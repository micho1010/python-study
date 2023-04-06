#向上面的乘法表程序中再加些代码，在询问用户想显示哪个数字的乘法表
#之后，再问问用户希望最大乘到哪个数字。输出结果应该如下所示:




#在编写第1题中的程序时，你可能使用了for循环(大多数人会这么做)，现在再用 while 循环来编写这个程序。
#(如果已经使用了 while 循环，可以试 着用 for 循环来编写。)
num = int(input("你想要哪个数字呀？"))
high = int(input("你希望最大乘到哪个数字？"))
count = 1
while count < high + 1 :
    print(num, "*", count, "=", count * num)
    count = count + 1



#编写一个程序，显示一张乘法表。
#在开始时要询问用户想显示哪个数字的乘法表，输出结果应该如下所示。

num = int(input("你想要哪个数字呀？"))
for loop in range(1,10):
    print(num, "*", loop, "=",num * loop)
print(*range(8))

for i in range(1, 6): 
    print('i =', i, ' ','Hello, how ', end='') 
    if i == 3:
        continue
    print('are you today?') 
print()