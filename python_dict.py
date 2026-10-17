student = {"name": "John", "age": 20, "grade": "A"}

print(student)
print(student["name"])

student["grade"] = "AA+"

print(student)

student["city"]="Delhi"

print(student)

friend =[{"name": "David", "Phone": "77889920", "grade": "A"},
         {"name": "Bob", "Phone": "78990020", "grade": "A"},
         {"name": "John", "Phone": "68899020", "grade": "A"}]
# for i in friend.keys():
#     friend.key(i)
# print(friend.values())

# you can also access through key,value pair
for i in friend:
    for key,value in i.items():
        print(f"{key} : {value}")