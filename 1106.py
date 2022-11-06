start = int(input("起始值："))
end = int(input("结束值："))


for num1 in range(start, end + 1):
    print("----------")
    if start <= 5:
        for i in range(9, 0, -1):
            print(num1, "*", i, "=", num1 * i)

    else:
        for j in range(1,10):
            print(num1, "*", j, "=", num1 * j)

