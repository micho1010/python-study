# import time
# for i in range(10,1,-1):
#     print(i)
#     time.sleep(1)
# print('BLAST OFF!')

# for letter in 'hi there':
#     print(letter, end='')

# for coolGuy in ['ChenNan','Ming']:
#     print(coolGuy,'is the coolest guy in the world!')

# print('Type 3 to continue, anything else to quit.')
# someInput = input()
# while someInput == '3':
#     print('Thank you for the 3. Very kind of you.')
#     print('Type 3 to continue, anything else to quit.')
#     someInput = input()
# print("That's not 3 ,so I'm quit now.")

# num = int(input('Which multiplication table would you like?'))
# for i in range(1,10):
#     print(num,"*",i,"=",i * num)

num = int(input('Which multiplication table would you like?'))
num0 = int(input('How high do you want to go?'))
times = 1
while  times <= num0:
    print(num,"*",times,"=",times * num)
    times += 1


# num = int(input("你想要哪个数字呀？"))
# high = int(input("你希望最大乘到哪个数字？"))
# count = 1
# while count < high + 1 :
#     print(num, "*", count, "=", count * num)
#     count = count + 1
