import wust
print(input("enter") in "gy")

url = r'http://jwxt.wust.edu.cn/whkjdx/xkglAction.do?method=toXk&xnxq=2018-2019-2&zzdxklbname=9&type=1&xkkssj=2019-03-01%2014:15&xkjzsj=2019-03-06%2014:30&jx0502id=85&jx0502zbid=149&xkfs=0&tktime=1551446958000'
print(url)

#wust.GetCoursesList()
wust.GetCoursesListByUrl(url)