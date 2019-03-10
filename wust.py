import requests
import re
import time
from bs4 import BeautifulSoup
import Model

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
}
foo = requests.session()

def GetRandCode(path = 'randcode.jpg'):
    url = r'http://jwxt.wust.edu.cn/whkjdx/verifycode.servlet'
    ans = foo.get(url)
    ans.raise_for_status()
    with open(path, 'wb') as file:
        file.write(ans.content)

def Login(username, password, randcode):
    url = r'http://jwxt.wust.edu.cn/whkjdx/Logon.do?method=logon'
    SSOurl = r'http://jwxt.wust.edu.cn/whkjdx/Logon.do?method=logonBySSO'
    information = {'USERNAME': username, 'PASSWORD': password, 'RANDOMCODE': randcode}
    ans = foo.post(url, data = information, headers = headers)
    ans.raise_for_status()
    ans.encoding = ans.apparent_encoding
    ans2 = foo.post(SSOurl, headers)
    ans2.raise_for_status()
    if ans.text.find(r'http://jwxt.wust.edu.cn/whkjdx/framework/main.jsp') != -1:
        return True
    else:
        return False

def GetKechengListByUrl(url):
    link = GetframeLink(url)

    kecheng = []

    ans = foo.get(link, headers=headers)
    ans.raise_for_status()
    ans.encoding = ans.apparent_encoding

    soup = BeautifulSoup(ans.text)

    kechengList = soup.find_all(class_ = "smartTr")

    for ke in kechengList:
        tds = BeautifulSoup(str(ke)).find_all("td")
        kec = Model.kecheng()

        kec.name = BeautifulSoup(str(tds[1])).text
        kec.xf = BeautifulSoup(str(tds[4])).text
        kec.teacher = BeautifulSoup(str(tds[7])).td['title']
        kec.zhouci = BeautifulSoup(str(tds[8])).text
        kec.time = BeautifulSoup(str(tds[9])).text
        link = str(BeautifulSoup(str(BeautifulSoup(str(tds[15])).find("a"))).a['onclick'])
        kec.xuankeLink = link.split("'")[1]

        kecheng.append(kec)

    return kecheng


def GetCoursesListByUrl(url):

    link = GetframeLink(url)

    ans = foo.get(link,headers = headers)
    ans.raise_for_status()
    ans.encoding = ans.apparent_encoding
    #print(ans.text)
    CoursesList = re.findall(r'<td height="23"  style="text-overflow:ellipsis; white-space:nowrap; overflow:hidden;" width="\d+" title=".*"',ans.text)
    XKLJList = re.findall("javascript:vJsMod\(\'.*\'", ans.text)
    keyname = ['kcmc', 'kkdw', 'zyfx', 'xf', 'yxrs', 'yl', 'skjs', 'skzc', 'sksj', 'skdd', 'kcsx', 'kcxz', 'fzm','xbyq']
    result = []
    item = {}
    bar = 0
    index = 0
    for i in CoursesList:
        Left = i.find(r'title="')
        Right = i[Left + 7:].find(r'"')
        text = i[Left + 7:Left + Right + 7]
        # print(i)
        # print(text)
        item[keyname[bar]] = text
        bar = bar + 1
        if (bar == 14):
            Left = XKLJList[index].find("'")
            Right = XKLJList[index][Left + 1:].find("'")
            text = XKLJList[index][Left + 1:Left + Right + 1]
            item['xklj'] = text
            index = index + 1

            result.append(item)
            item = {}
            bar = 0
    return result

def GetframeLink(url):
    ans = foo.get(url,headers = headers)
    ans.raise_for_status()
    ans.encoding = ans.apparent_encoding

    #print(ans.text)

    soup = BeautifulSoup(ans.text)
    frame = soup.find(id = "mainFrame")

    #print(frame)

    link = "http://jwxt.wust.edu.cn" + str(BeautifulSoup(str(frame)).frame['src']).replace(' ','%20')

    #print(link)

    ans1 = foo.get(link,headers = headers)
    ans1.raise_for_status()
    ans1.encoding = ans1.apparent_encoding

    soup1 = BeautifulSoup(ans1.text)

    frame1 = soup1.find(id = "centerFrame")

    link1 = "http://jwxt.wust.edu.cn" + str(BeautifulSoup(str(frame1)).frame['src']).replace(' ','%20')

    #print(link1)

    return link1


def GetXuankeList():

    url = r'http://jwxt.wust.edu.cn/whkjdx/xkglAction.do?method=xsxkXsxk&tktime=1551747139000'

    result = []

    #url = r'http://jwxt.wust.edu.cn/whkjdx/xkglAction.do'
    # pa = {"method":"xsxkXsxk","tktime":str(int(time.time() * 1000))}
    #
    # print(pa.get("tktime"))

    ans = foo.get(url,headers = headers)

    ans.raise_for_status()
    ans.encoding = ans.apparent_encoding

    soup = BeautifulSoup(ans.text)

    Xuankelist = soup.find_all(class_ = "smartTr")

    for xuankeL in Xuankelist:
        xuank = Model.xuanke()

        td = BeautifulSoup(str(xuankeL))

        tds = td.find_all("td")

        xuank.index_ = BeautifulSoup(str(tds[0])).text

        xuank.xueqi = BeautifulSoup(str(tds[1])).text

        xuank.name_ = BeautifulSoup(str(tds[2])).text

        xuank.jieduan_ = BeautifulSoup(str(tds[3])).text

        xuank.StartTime = BeautifulSoup(str(tds[4])).text

        xuank.EndTime = BeautifulSoup(str(tds[5])).text

        #xuank.Link = BeautifulSoup(str(tds[6])).a['onclick']

        strs = str(BeautifulSoup(str(tds[6])).a['onclick']).split("'")

        xuank.Link = strs[1]

        result.append(xuank)

        # print(xuank.name_)
        # print(xuank.Link)

    return result



# def GetCoursesList():
#     url = r'http://jwxt.wust.edu.cn/whkjdx/xkglAction.do?method=toXk&xnxq=2018-2019-2&zzdxklbname=9&type=1&xkkssj=2019-03-01%2014:15&xkjzsj=2019-03-06%2014:30&jx0502id=85&jx0502zbid=149&xkfs=0&tktime=1551446958000'
#     ans = foo.get(url, headers = headers)
#     ans.raise_for_status()
#     ans.encoding = ans.apparent_encoding
#     print(ans.text)
#     CoursesList = re.findall(r'<td height="23"  style="text-overflow:ellipsis; white-space:nowrap; overflow:hidden;" width="\d+" title=".*"', ans.text)
#     XKLJList = re.findall("javascript:vJsMod\(\'.*\'", ans.text)
#     keyname = ['kcmc', 'kkdw', 'zyfx', 'xf', 'yxrs', 'yl', 'skjs', 'skzc', 'sksj', 'skdd', 'kcsx', 'kcxz', 'fzm', 'xbyq']
#     result = []
#     item = {}
#     bar = 0
#     index = 0
#     for i in CoursesList:
#         Left = i.find(r'title="')
#         Right = i[Left + 7:].find(r'"')
#         text = i[Left + 7:Left + Right + 7]
#         #print(i)
#         #print(text)
#         item[keyname[bar]] = text
#         bar = bar + 1
#         if (bar == 14):
#             Left = XKLJList[index].find("'")
#             Right = XKLJList[index][Left + 1:].find("'")
#             text = XKLJList[index][Left + 1:Left + Right + 1]
#             item['xklj'] = text
#             index = index + 1
#
#             result.append(item)
#             item = {}
#             bar = 0
#     return result

def ChoseCourseByLink(link):
    url = 'http://jwxt.wust.edu.cn' + link
    ans = foo.get(url, headers = headers)
    ans.raise_for_status()
    ans.encoding = ans.apparent_encoding
    return ans.text

def getRandomUrl(htmlurl):
    count = str(htmlurl).find('?')

    t = str(int(time.time() * 1000))

    if count<0:
        htmlurl = htmlurl + "?tktime=" + t;
    else:
        htmlurl = htmlurl + "&tktime=" + t;

    return htmlurl