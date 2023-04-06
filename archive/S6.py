
# arr = [1, 2, 3]
# for value in arr:
#     print('v', value)

# print(list(stu.keys()))
# 遍历
stu = {
    'name': 'Ming',
    'age': '8',
    'address': 'sanlitun'
}

# for key in stu:
#     print(f'key: {key}, value: {stu[key]}')

# for key in stu.keys():
#     print(f'key: {key}, value: {stu[key]}')

# for value in stu.values():
#     print(f'value: {value}')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

values = favorite_languages.values()
for value in sorted(values):
    print(f"{value}, thank you for taking the poll.")

# for item in stu.items():
#     print('item', item)
#     print('key', item[0])
#     print('value', item[1])

# # print(list(stu.values()))
# # print(list(stu.items()))

# # print(stu.get('gender','f'))
# # # # print(f"student's name is: {stu['name']}")
# # # # stu['age'] = int(stu['age']) + 3
# # # # print(f"the student's age is: {stu['age']}")

# # alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

# # print(f"Original position: {alien_0['x_position']}")

# # x_increment = 0
# # if alien_0['speed'] == 'slow':
# #     x_increment = 1
# # elif alien_0['speed'] == 'medium':
# #     x_increment = 2
# # else:
# #     x_increment = 3

# # alien_0['x_position'] = alien_0['x_position'] + x_increment
# # print(f"New position: {alien_0['x_position']}")
