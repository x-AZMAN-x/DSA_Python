class Dog:
    #Class Sttribute: Shared By All Instances/Objects
    breed = "German Sphepard"
    #Constructor: Initializes The Objects
    def __init__(self, name, age):
        #Instance Attributes: Unique To All Objects
        self.name = name
        self.age = age

        #Methods Are Functions That Are Defoned Inside A Class
        #Instance Method
    def bark(self):
        return (f"{self.name} Barks!")
    
#Creating Objects/Instances
dog1 = Dog("Max", 5)
dog2 = Dog("Maxxy", 4)

#Accesing Attributes
print(f"The First Dog's Name Is {dog1.name}. His Age Is {dog1.age}.")
print(f"The Second Dog's Name Is {dog2.name}. Her Age Is {dog2.age}.")
print(f"Both Of Their Breed Is {Dog.breed}.")

#Calling Methods
print(f"{dog1.bark()}")
print(f"{dog2.bark()}")