import wust
import time
import Model

scc = "该课程不能重复选择"
scc1 = "选课成功"

def qiangke1(urls):
    for url in urls:
        while True:
            try:
                text = wust.ChoseCourseByLink(url)
            except:
                print('抢课失败，进行下一次尝试')
            else:
                if scc1 in text or scc in text:
                    print('选课成功')
                    print(text)
                    break;
                print('抢课失败，进行下一次尝试')
                # print(text)
            # time.sleep(1)
            time.sleep(0.5)

def qiangke2(link,kcmc,skjs,sksj,skzc,xf):
    # tree.insert("", index, text = i['kcmc'], values = (i['skjs'], i['sksj'], i['skzc'], i['xf']))
    # 循环获取公选课列表直至成功
    UrlList = []

    link = 'http://jwxt.wust.edu.cn'+str(wust.getRandomUrl(link)).replace(' ','%20')
    #print(link)
    while True:
        try:
            # 登录成功之后获取公选课列表，因为桥牌是公选课
            List = wust.GetCoursesListByUrl(link)
            #wust.GetframeLink(link)
        except:
            print('抓取公选课列表失败，进行下一次尝试')
        else:
            print('抓取公选课列表成功，即将进行抢课')
            break

    for i in List:
        #print(i['kcmc']+i['skjs']+i['sksj'])
        # 筛选课程条件，还可以对时间或者其他信息进行筛选，只需要改变条件
        if (kcmc in i['kcmc']) and (skjs in i['skjs']) and (sksj in i['sksj']) and (skzc in i['skzc']) and (xf in i['xf']):
            UrlList.append(i['xklj'])
            print(i['kcmc'] + i['skjs'] + i['sksj'])

    qiangke1(UrlList)

# 循环获取验证码直至成功
while True:
    try:
        wust.GetRandCode('randcode.jpg')
        # 要求用户输入验证码
        randcode = input('Please input the Random Code:')
    except:
        print('获取验证码失败，进行下一次尝试')
    else:
        print('获取验证码成功，即将尝试登录')
        break

# 循环登录直至成功
while True:
    try:
        # 保存登录状态
        login_status = wust.Login('201701145013', 'fgy18897514992', randcode)
        while not login_status:
            # 登录失败，重新获取验证码
            wust.GetRandCode('randcode.jpg')
            # 重新要求用户输入验证码
            randcode = input('Please input the Random Code:')
            # 重新保存登录状态并登录
            login_status = wust.Login('201701145013', 'fgy18897514992', randcode)
    except:
        print('教务处网络状态差，尝试登录失败，进行下一次尝试')
    else:
        print('登录成功，即将抓取公选课列表')
        break

Xuanlist = wust.GetXuankeList()
index = 0
for i in Xuanlist:
    print(str(index)+" "+i.name_)
    index = index+1

index = int(input("enter index:"))

#kcmc,skjs,sksj,skzc,xf

kcmc = input("enter kcmc")#课程名称
skjs = input("enter skjs")#上课教师
sksj = input("enter sksj")#上课时间
skzc = input("enter skzc")#上课周次
xf = input("enter xf")#学分

#print(kcmc+skjs+sksj+skzc+xf)

qiangke2(Xuanlist[index].Link,kcmc,skjs,sksj,skzc,xf)
