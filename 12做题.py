



stu = {
    "name": "2",
    "gender": "3",
    "phone": "1",
    # "colors": ["红", "蓝", "白"],
    # "comment": {
        # "message": "这是个可爱的孩子"
    # }
}
# print(list(stu.keys()))
# print(stu["colors"][2])
for value in sorted(stu.values()):
    for key in stu.keys():
        if stu[key] == value: 
            print(key, stu[key])