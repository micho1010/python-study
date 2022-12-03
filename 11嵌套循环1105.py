import time
count = int(input("你这个炸弹犯，说还有几秒钟爆炸！"))
for i in range(count, 0, -1):
    print(i)
    time.sleep(1)
print("BLAST OFF!")

for i in range(5):
    for j in range(3):
        print('* ', end='')
print()


numLines = int(input('How many lines of stars do you want? '))
numStars = int(input('How many stars per line? '))
for line in range(0, numLines):
    for star in range(0, numStars):
        print('* ', end='')
    print("~~~~~~~~~~~~~~")

for multiplier in range(5, 8):
    for i in range(1, 11):
        print(i, "×", multiplier, "=", i * multiplier)


num1 = int(input("数字"))
for num2 in range(1, 10):
    print(num1, "*", num2, "=", num1 * num2)
