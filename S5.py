# 作业
# 现在有一份安全配色列表
# colors = ['red', 'green', 'blue']
# 要求用户从命令行输入一个颜色，判断用户输入的颜色是否是安全色
# 如果是安全色，print 输出 “safe, color is: xxx”
# 如果不是则 print 输出 “danger, color is: xxx”

colors = ['red', 'green', 'blue']
newColor = input("你想要什么颜色：")
# if newColor in colors:
#     print(f"safe color is:{newColor}")
# else:
#     print(f"danger, color is: {newColor}")

for currentColor in colors:
    if newColor == currentColor:
        print(f"safe color is:{newColor}")
    else:
        print(f"danger, color is: {newColor}")