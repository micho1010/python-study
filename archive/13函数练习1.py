# 编写一个函数，统计一堆零钱的总值，这些零钱中包括 1 分、1 角和 1 元，
# 类似于第 5 章“动手试一试”中的最后一个问题。这个函数应该返回这些硬 币的总值，
# 然后再编写一个程序来调用这个函数。
# 当运行程序时，可以看到 类似下面的输出结果。

fen = int(input('你有几分钱？'))
jiao = int(input('你有几角钱？'))
yuan = int(input('你有几元钱？'))


def sum(fen, jiao, yuan):
    total = fen * 0.01 + jiao * 0.1 + yuan
    return total


totalmoney = sum(fen, jiao, yuan)
print('你总共有多少钱？', totalmoney)
