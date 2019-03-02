import requests
import re

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

# def GetCoursesList():
#     url = r'http://jwxt.wust.edu.cn/whkjdx/xkglAction.do?method=toFindxskxkclb&xnxq01id=2017-2018-2&zzdxklbname=1&type=1&jx02kczid=null'
#     ans = foo.get(url, headers = headers)
#     ans.raise_for_status()
#     ans.encoding = ans.apparent_encoding
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

def GetCoursesListByUrl(url):

    ans = foo.get(url,headers = headers)
    ans.raise_for_status()
    ans.encoding = ans.apparent_encoding
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


def GetCoursesList():
    url = r'http://jwxt.wust.edu.cn/whkjdx/xkglAction.do?method=toXk&xnxq=2018-2019-2&zzdxklbname=9&type=1&xkkssj=2019-03-01%2014:15&xkjzsj=2019-03-06%2014:30&jx0502id=85&jx0502zbid=149&xkfs=0&tktime=1551446958000'
    ans = foo.get(url, headers = headers)
    ans.raise_for_status()
    ans.encoding = ans.apparent_encoding
    CoursesList = re.findall(r'<td height="23"  style="text-overflow:ellipsis; white-space:nowrap; overflow:hidden;" width="\d+" title=".*"', ans.text)
    XKLJList = re.findall("javascript:vJsMod\(\'.*\'", ans.text)
    keyname = ['kcmc', 'kkdw', 'zyfx', 'xf', 'yxrs', 'yl', 'skjs', 'skzc', 'sksj', 'skdd', 'kcsx', 'kcxz', 'fzm', 'xbyq']
    result = []
    item = {}
    bar = 0
    index = 0
    for i in CoursesList:
        Left = i.find(r'title="')
        Right = i[Left + 7:].find(r'"')
        text = i[Left + 7:Left + Right + 7]
        #print(i)
        #print(text)
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

def GetCoursesList2():
    url = r'http://jwxt.wust.edu.cn/whkjdx/xkglAction.do?method=toFindxskxkclb&xnxq01id=2017-2018-2&zzdxklbname=6&type=1&jx02kczid=null'
    ans = foo.get(url, headers = headers)
    ans.raise_for_status()
    ans.encoding = ans.apparent_encoding
    CoursesList = re.findall(r'<td height="23"  style="text-overflow:ellipsis; white-space:nowrap; overflow:hidden;" width="\d+" title=".*"', ans.text)
    XKLJList = re.findall("javascript:vJsMod\(\'.*\'", ans.text)
    keyname = ['kcmc', 'kkdw', 'zyfx', 'xf', 'yxrs', 'yl', 'skjs', 'skzc', 'sksj', 'skdd', 'kcsx', 'kcxz', 'fzm', 'xbyq']
    result = []
    item = {}
    bar = 0
    index = 0
    for i in CoursesList:
        Left = i.find(r'title="')
        Right = i[Left + 7:].find(r'"')
        text = i[Left + 7:Left + Right + 7]
        #print(i)
        #print(text)
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

def ChoseCourseByLink(link):
    url = 'http://jwxt.wust.edu.cn' + link
    ans = foo.get(url, headers = headers)
    ans.raise_for_status()
    ans.encoding = ans.apparent_encoding
    return ans.text
