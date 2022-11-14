def calculateTax(price, taxRate):
    total = price + (price * taxRate)
    # newPrice = myPrice
    myPrice = 12
    print(myPrice)
    return total


# print(calculateTax(100, 0.123))
myPrice = float(input('Enter a price:'))
totalPrince = calculateTax(myPrice, 0.06)
print('price = ', myPrice, 'Total price = ', totalPrince)


def printMyAddress(myName):
    print(myName)
    print('124')
    print('Ottawa, Ontario, Canada')
    print()

# printMyAddress('XiaoBai')
