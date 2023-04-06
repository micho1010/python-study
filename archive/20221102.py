# 实现一个程序，录入学生的姓名、性别、年纪、与喜欢颜色（红、黄、蓝等，单个字）
# 如果学生的年龄小于 20 岁，那么输出 （XX 喜欢 XX 颜色）
# 如果学生的年龄大于等于 20 岁，
# 如果其性别为【男】且颜色为【粉】，则输出“XX 猛男喜欢的颜色为 XX”，
# 如果性别为【女】其颜色不为"黑"或者"白"，则输出 ”XX 喜欢 XX 颜色“，否则都输出 ”xx 随便喜欢 xx 颜色“

name = input("姓名：")
age = int(input("年纪："))
gender =input("性别(写f或者m)")
color = input("你最喜欢的颜色(请输入红、黄、蓝等单个字):")

if age < 20:
    print(name, "喜欢", color, "颜色")
if age >= 20 and gender == "m" and color == "粉":
    print(name, "猛男喜欢的颜色为", color)
if  age >= 20 and gender == "f" and color != "黑" and color != "白":
    print(name, "喜欢", color)
else:
    print(name, "随便喜欢",color, "颜色")

name1 = input("姓名：")
age1 = int(input("年纪："))
gender1 =input("性别(写f或者m)")
color1 = input("你最喜欢的颜色(请输入红、黄、蓝等单个字):") 

if age < 20:
    print(name, "喜欢", color, "颜色")
else:
    if gender1 == 'm' and color1 == '粉':
        print(name1, "猛男喜欢的颜色为", color1)
    if gender1 == "f" and color1 != "黑" and color1 != "白":
        print(name1, "仙女喜欢", color1)
    else:
        print(name1, "随便喜欢", color1)
print("done")

