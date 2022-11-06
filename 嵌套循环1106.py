import time
num = int(input("你希望几点开始倒数："))
for starline in range(num,0,-1):  
    print(starline, end="")
    for star1 in range(starline):
        print("*", end="")
    time.sleep(1)
    print()
    
print("boom！！！")
