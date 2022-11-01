# 从终端输入，输入颜色，颜色不限，输入的颜色例如：红、旅、蓝、黄
# 如果颜色是“紫”，那么输出“小可爱最喜欢的颜色”
# 如果颜色是“蓝”，那么输出“猛男最爱”
# 如果颜色是“黑” 或 “白”，那么输出“世界的基础”
# 如果是其他颜色，则输出“滚”

color = input("请输入任意一个颜色，如红、绿、蓝、黄等")
if color == "紫":
    print("小可爱最喜欢的颜色")
elif color == "蓝":
    print("猛男最爱！")
elif color == "黑" or color == "白":
    print("世界的基础")
else:
    print("滚😡")


num1 = float(input("请输入你想要的数字："))
num2 = float(input("乘以几："))
print("这是您想要的结果：",num1 * num2)

print("我真可爱！", "放假真美啊！", "可怜的大可爱不想上班，让我们一起默哀一秒钟！")

good = "shikgng" + "shi"
print(good)

print(1 + 2)
print(1 + 2.0)
print("shikgng" + "jiughisk")
print(str(100) + "jsdfgh")
print(str(1.23) + "jiushigkg")