#假设你正在开车长途旅行，这时刚到一个加油站，距离下一个加油站还有 200 千米。编写一个程序，
# 判断是否应该在这里加油，换句话说，是否可以 等到抵达下一个加油站再加油。
# 这个程序应当询问下面几个问题。
# 油箱有多大(单位是升)?现在油箱有多满(按百分比算，例如半满就是 50%)?  每升油可以走多少千米?


sizeOfTank = float(input("仅输入数字，单位是升")) - 5
percentFull = float(input("你的车车饿了吗？"))
per = float(input("每升油可以走多少千米"))
canIContinueThisTrip = sizeOfTank * percentFull * per 
if canIContinueThisTrip >= 200:
    print("加油！继续前行吧")
else:
    print("不加油，你们都会饿死哒！")

#2. 一支少儿足球队在寻找年龄在 10 岁和 12 岁之间的女孩加入。编写一个程序， 
#询问用户的年龄和性别(m 表示男性，f 表示女性)，最后输出一条消息说明 该用户是否可以加入球队。
#提示:要合理地编写程序，如果用户不是女孩， 就不必再询问年龄。

age = int(input("您贵庚呀？"))
gender = input("f or m")
if gender != "m" and age >=10 and age<=12:
    print("恭喜你加入女子足球队")
else:
    print("Get out!")




#1. 一家商店在降价促销:购买金额小于或等于 10 元享 9 折优惠，购买金额大于 10 元享 8 折优惠。
#编写一个程序，询问购买金额，然后显示优惠方案(9 折 或 8 折)和最终价格。

price = int(input("贵客今天花了多少钱？"))
if price <= 10:
    print("您实际需要付：",price * 0.9)
else:
    print("天呐！您真有钱钱！", price * 0.8)

#4. 如果要检查用户输入的字母是大写还是小写(比如是 Q 还是 q)，应该使用哪一种 if 语句?


value = "b"
if value == "A":
    print(value, "这是大写")
elif value == "b":
    print(value, "这不是大写")



my_number = 7
if my_number < 20:
    print("Under 20") 
else:
    print("20 or over")
#如果要检查一个数是否大于 30 且不超过 40，应该用哪一种 if 语句?
num = 35
if num >30 and num <= 40:
    print("The number is greater than 30 ")



answer = float(input("Enter a number from 1 to 15: "))

if answer >= 10:
    print("You got at least 10!")
elif answer >= 7:
    print("You got at least 7! ")
elif answer >= 5:
    print("You got at least 5!")
elif answer >= 3:
    print("You got at least 3!")
else:
    print("You got less than 3.")



num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))

if num1 < num2:
    print(num1, "is less than", num2)
if num1 > num2:
    print(num1, "is greater than", num2)
if num1 == num2:
    print(num1, "is equal to", num2)
if num1 != num2:
    print(num1, "is not equal to", num2)