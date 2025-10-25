class Cat:
    def __init__(self, name, age):
      self.name = name
      self.age = age
      
    def info(self):
      print(f"I Am A Cat. My Name Is {self.name}. I Am {self.age} Years Old.")

    def sound(self):
      print("Meow")
    
class Dog:
    def __init__(self, name, age):
      self.name = name
      self.age = age
      
    def info(self):
      print(f"I Am A Dog. My Name Is {self.name}. I Am {self.age} Years Old.")

    def sound(self):
      print("Woof")

cat = Cat("Tom", 3)
dog = Dog("Max", 4.5)

for animal in [cat, dog]:
   animal.sound()
   animal.info()