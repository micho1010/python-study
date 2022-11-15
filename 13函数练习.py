# 编写一个函数，统计一堆零钱的总值，这些零钱中包括 1 分、1 角和 1 元， 类似于第 5 章“动手试一试”中的最后一个问题。
# 这个函数应该返回这些硬 币的总值，然后再编写一个程序来调用这个函数。
# 当运行程序时，可以看到 类似下面的输出结果。



# 不过要让my_price变为全局变量，看看输 出结果有什么不同。

# def calculateTax(price, tax_rate):
#     global my_price
#     total = price + (price * tax_rate)
#     my_price = 10000
#     print("my_price (inside function) = ", my_price)
#     return total


# my_price = float(input("Enter a price: "))

# totalPrice = calculateTax(my_price, 0.06)
# print("price = ", my_price, " Total price = ", totalPrice)
# print("my_price (outside function) = ", my_price)


# 定义一个函数，可以打印出全世界任何人名、住址、街道、城市、省份(州)、 邮政编码和国家。
# (提示:这里需要 7 个参数。你可以把它们作为单独的参数依次传递，也可以作为一个列表整体传递。)

# def message(params):
    # print("name:", params["name"])
    # print("address:", params["address"])
    # print("street:", params["street"])
    # print("city:", params["city"])
    # print("province:", params["province"])
    # print("code:", params["code"])
    # print("country:", params["country"])

# # params0 = {
#     "name": "Mei",
#     "address": "Beijing",
#     "street": "中华路",
#     "city": "哥谭市",
#     "province": "通辽省",
#     "code": "350000",
#     "country": "中国"
# }
# message(params0)
