class Animal:
    country = "ANG"

    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def speak(self):
        print("Animal callling====")   

class Dog(Animal):

    def __init__(self, name, breed,age):
        super().__init__(name, breed)
        self.age = age

    def speak(self):
        super().speak()
        print("Blooo blooo") 

d1 = Dog("brumo","chii",2)

print(d1.name,d1.breed,d1.age)

d1.speak()



