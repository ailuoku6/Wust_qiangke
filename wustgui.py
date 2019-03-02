import tkinter
import wust
from tkinter import ttk

wust.GetRandCode()
randcode = input()
wust.Login('201701145013', 'fgy18897514992', randcode)

CousList = wust.GetCoursesList()

win = tkinter.Tk(className='武科大教务抢课')

tree = ttk.Treeview()
tree["columns"] = ("上课教师", "上课时间", "上课周次", "学分")  
tree.column("上课教师",width=100)   #表示列,不显示  
tree.column("上课时间",width=100) 
tree.column("上课周次",width=100)
tree.column("学分",width=100)

tree.heading("上课教师",text="上课教师")  #显示表头  
tree.heading("上课时间",text="上课时间")  
tree.heading("上课周次",text="上课周次")
tree.heading("学分",text="学分")

index = 0
for i in CousList:
    tree.insert("", index, text = i['kcmc'], values = (i['skjs'], i['sksj'], i['skzc'], i['xf']))
    index = index + 1

tree.pack()  
win.mainloop()
