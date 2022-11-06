start = int(input("起始值："))
end = int(input("结束值："))

for num1 in range(start, end + 1):
    print("----------")
    for num2 in range(1,10):
        print(num1, "*", num2, "=", num1 * num2)