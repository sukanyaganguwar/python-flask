
# my_set = {1, 2, 3, 3, 4}

# print(my_set)

# my_set.add(5)

# print(my_set)

# my_set.remove(2)

# print(my_set)

# a = {1,2,3}
# b = {3,4,5}

# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))



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
for i in friend:
    for key,value in i.items():
    #    print(f"{i} --> {i.get(key)}")
    #    print(f" {key} == {value}")
        print(value)

print()
print("=============================================")
# interating with key

for key in student:
    print(f"key : {key}") 

print()
print()

#intearting through value

for i in student.values():
     print(f"value : {i}") 

print()
print()     

for key,value in student.items():
    print(f" key: {key}  value:{value}")     
