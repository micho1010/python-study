#编写一个程序，询问一间矩形房间的尺寸(单位是米)，然后计算并显示铺满整个房间总共需要多少地毯，单位是平方米。

width = input("宽是多少")
height = input("长是多少")
area = int(width) * int(height)
print("整个房间面积为",area)
price = input("地毯的价格是多少？")
area1 = 9 * area
print("总共需要多少平方尺的地毯", area1)
totalPrice = area1 * int(price)
print("地毯的总价格", totalPrice)



#4. 编写一个程序，完成第 3 题的要求，并且询问每平方尺地毯的价格。然后主程序显示下面 3 项内容。
#总共需要多少地毯，单位是平方尺(1 平方米 = 9 平方尺)。
#地毯的总价格。



#5. 编写一个程序，帮助用户统计一些零钱。程序要问下面的问题。
#“有多少枚 1 分”
#有多少枚 1 角?”
#“有多少枚 1 元?” 让程序给出这些零钱的总值(单位是元)。

fen = input("你有多少枚1分")
jiao = input("你有多少枚1角")
yuan = input("你有多少枚1元")
totalmoney = int(fen) /100 + int(jiao) / 10 + int(yuan)
print("恭喜你！你穷到零钱了，你总共有", totalmoney, "元钱, 加油赚钱吧！")



#1. 在交互模式中创建两个变量，分别表示你的姓氏和名字。然后使用一条 print() 语句，把它们打印在一起。
#2. 编写一个程序，先问你的姓氏，再问你的名字，然后打印出一条消息，其中 包含你的姓名。

firstName = input("请输入你的姓")
lastName = input("请输入你的名")
print(firstName, lastName)

someName = input("Enter your name:")
print('someName', someName)

numberOfStudents = int(input("How many students are in your class:"))
print(numberOfStudents)


