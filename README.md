# 武科大教务抢课（半成品）

目前已经完成了 wust 库，大概就是有这么几个函数：

`GetRandCode` 用来获取验证码，获取验证码之后通过 `Login` 登录，然后通过 `GetCoursesList` 可以获取公选课列表，`GetCoursesList2` 可以获取学分制选课列表，这个列表每一项都是一个包含选课十五个信息的字典，其中键 `xklj` 是选这个课的链接，把这个链接传到 `ChoseCourseByLink` 可以选这个课。

一个简单的抢桥牌的例子（`demo_自动选桥牌.py`），用于抢桥牌课。

`wustgui.py` 是使用这个库的一个简单例程。



![wustgui](https://raw.githubusercontent.com/Rugel/wustjwxt/master/wustgui.png)