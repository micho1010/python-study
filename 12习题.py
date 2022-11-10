# 编写一个程序，让用户输入 5 个名字。该程序要把这 5 个名字保存在一个列 
# 表中，然后打印出来，如下所示。
# name0 = input('请输入名字1')
# name1 = input('请输入名字2')
# name2 = input('请输入名字3')
# name3 = input('请输入名字4')
# name4 = input('请输入名字5')
# theName = [name0, name1, name2, name3, name4]
# print(theName)

# 修改第 1 题中的程序，不仅要打印出原来的名字列表，还要打印出排序后的列表。

# 修改第 1 题中的程序，要求只打印出用户输入的第 3 个名字，如下所示。

# 修改第 1 题中的程序，让用户替换其中的一个名字。保证用户能够随机选择 要替换的名字，
# 然后输入新的名字。最后打印出新列表，如下所示。


names = []

for item in range(1, 6):
    name = input('请输入姓名 ' + str(item))
    names.append(name)

print(names)

index = int(input('witch one?'))
newName = input('newName')
names[index] = newName
print(names)


words = {}

for item in range(3):
    key = input('输入单词')
    value = input('输入含义')
    words[key] = value

target = input('你要找的')

if target in words:
    print(target, '含义是', words[target])
else:
    print('not fond~')