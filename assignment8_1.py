class Employee:

    def __init__(self,salary):
        self._salary = salary


    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,new_salary):
        if new_salary > 0:
           self._salary = new_salary
        else:
            print("no negative value excepted")   


e = Employee(1000)
print(e.salary)
e.salary = -300
print(e.salary)

