import wust
import time

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
                if scc1 in text:
                    print('选课成功')
                    print(text)
                    break;
                if scc in text:
                    print('选课成功')
                    print(text)
                    break;
                print('抢课失败，进行下一次尝试')
                # print(text)
            # time.sleep(1)
            time.sleep(0.5)

def qiangke2(kcmc,skjs,sksj,skzc,xf):
    # tree.insert("", index, text = i['kcmc'], values = (i['skjs'], i['sksj'], i['skzc'], i['xf']))
    # 循环获取公选课列表直至成功
    UrlList = []
    while True:
        try:
            # 登录成功之后获取公选课列表，因为桥牌是公选课
            List = wust.GetCoursesList()
        except:
            print('抓取公选课列表失败，进行下一次尝试')
        else:
            print('抓取公选课列表成功，即将进行抢课')
            break

    for i in List:
        # 筛选课程条件，此处的条件是课程名称中含有桥牌，还可以对时间或者其他信息进行筛选，只需要改变条件
        if (kcmc in i['kcmc']) and (skjs in i['skjs']) and (sksj in i['sksj']) and (skzc in i['skzc']) and (xf in i['xf']):
            UrlList.append(i['xklj'])
            print(i)

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
        login_status = wust.Login('2017011450**', 'fgy18897514992', randcode)
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


        # if i['kcmc'].find(kcmc) != -1:
        #     # 筛选条件成立之后保存该课程的选课链接
        #     xklj = i['xklj']
        #     print('即将抢课所有信息如下：')
        #     print(i)
        #     break

# xklj1 = "/whkjdx/xkglAction.do?method=xsxk&xnxq01id=2018-2019-2&jx0502id=85&type=1&jx0504id=201820192013028&xf=3&kch=1401842&zxs=72&jx02kczid=null&zzdxklbname=9&szkcfl=&kcsx=1&kcsj=,409,410,,,209,210,&kczc=,4,5,6,7,8,9,10,11,12,13,14,15,,,4,5,6,7,8,9,10,11,12,13,14,15,&kksj=40910,20910&jx02id=02944&kcxzm=14"
#
# while True:
#     try:
#         text = wust.ChoseCourseByLink(xklj1)
#     except:
#         print('抢课失败，进行下一次尝试')
#     else:
#         if scc1 in text:
#             print('选课成功')
#             print(text)
#             break;
#         if scc in text:
#             print('选课成功')
#             print(text)
#             break;
#         print('抢课失败，进行下一次尝试')
#         # print(text)
#     # time.sleep(1)
#     time.sleep(0.5)