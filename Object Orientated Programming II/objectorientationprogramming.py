class Person:

    def __init__(self, name):
        self.name = name
        print(f"{self.name} Is Created.")
    
    def __del__(self):
        print(f"{self.name} Is Deleted.")

person1 = Person("Tom")

print(person1.name)
del person1
print(person1.name)