# 今天学了好多知识点：
# 1. 用f“字符串{变量}”的方式使句子更整洁
# 2. 用字符串自带的方法（函数）改变print呈现的效果
# 3. 数字+ - * /，并用print函数输出结果，“/”输出结果默认为浮点数


name = "Eric"
age = 8
code = "350725"
# print("Hello "+name+", would you like to learn some Python today?")
# print("这位是" + name + "，年龄为" + str(age) + "，身份证号码为" + code + "， 让我们恭喜ta成为新一轮韭菜！")
message = f"这位是 {name}，年龄为{age},身份证号码为{code} ，让我们恭喜ta中大奖啦！"
print(message)

my_name = "private Peaceful"
print(my_name.title())
print(my_name.upper())
print(my_name.lower())
# title\upper\lower这三个是字符串自带的方法（函数）

print(5 + 3)
print(10 - 2)
print(4 * 2)
print(16 / 2)

# 对字符串求长度
my_cat_name = "Python girl!"
print(len(my_cat_name))

# 通过索引获取单个字符
print(my_cat_name[5])
print(my_cat_name[len(my_cat_name)-1])

# 布尔类型
b1 = True
b2 = False

# 空值类型
n = None

# type函数
print(type(b1))
print(type(my_cat_name))
