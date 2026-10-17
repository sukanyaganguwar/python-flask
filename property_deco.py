class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @property
    def first_name(self):
        l = self.name.split(" ")  
        print(l)
        return l[0]  

    @first_name.setter
    def first_name(self,first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name

e1 = Employee("John Doe",34000)   

#old way
# print(e1.firstname())
# e1.set_firstname("Jack")
# print(e1.name)

# after getter setter
e1.first_name = "Jack"
print(e1.name)
