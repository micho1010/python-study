#编写一个程序，用户必须输入正确的密码才能使用这个程序。你自己当然知 道密码(你会将它写在代码中)，
#不过，你的朋友要知道这个密码就必须向你 求助或者直接猜密码，他也可以学习一定的 Python 知识，
#从而查看代码并找 到密码。
#程序本身没什么特别要求，既可以是你已经编写过的程序，也可以是新编写 的非常简单的程序，
#它必须在用户输入正确的密码时显示一条“You’re in!” 之类的消息.

secretCode = 23
yourCode = int(input("你猜的密码是？"))
if yourCode >= 30:
    print("You are close!")
if yourCode <= 20:
    print("It is to far!")
if yourCode == 23:
    print("You are in!")
else:
    print("You can pay 1 doller to me, I will tell you!")



print("小可爱真棒呀！\n" * 9)