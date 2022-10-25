from tkinter import E


a = 23
b = float(a)
print(b)

numberA = 2234.005
numberB = int(2234)
print("这是numbera的输出",type(numberB))

e = 34354
f = str(e)
print("f的值是",f)

'''如何只用int()函数对一个数字四舍五入而不是向下取整?(例如，
13.2 会向下取整为 13，但是 13.7 会向上取整为 14。)'''

value1 = 88.6
print("向上取整", int(value1 + 0.5))

value1 = "3.2"
value2 = "2.3"
value3f = float(value1)
value3 = int(value3f)
value4f = float(value2)
value4 = int(value4f)
res = value3 * value4
print("res的值:",res)

value6 = '3.13'
value7 = '454.67'
print(int(float(value6) * float(value7)))