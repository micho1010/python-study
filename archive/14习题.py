# 定义一个BankAccount类，它有一些属性，包括账户名(一个字符串)、
# 账号(一 个字符串或整数)和余额(一个浮点数)，另外还要有一些方法来
# 显示余额， 或者执行存取款操作。

class BankAccount:
    def __init__(self, name, account, money):
        self.name = name
        self.account = account
        self.money = money

    def yourMoney(self):
        print('你的余额:', self.money)

    def saveMoney(self, addMoney):
        totalMoney = self.money + addMoney
        self.money = totalMoney
    
    def takeMoney(self, giveMoney):
        residueMoney = self.money - giveMoney
        self.money = residueMoney


myBankAccount = BankAccount('XU', 'abc', 99999999)
myBankAccount.yourMoney()
myBankAccount.saveMoney(1)
myBankAccount.yourMoney()
myBankAccount.takeMoney(99999999)
myBankAccount.yourMoney()
