class Robot:
    color = "white"
    def __init__(self, name, Type):
        self.name = name
        self.type = Type

robot1 = Robot("John", "Vaccum Cleaner")
robot2 = Robot("Jhonathon", "Computer")

print(f"This Robot Was Named As {robot1.name}, And His Type Was Defined As {robot1.type}.")
print(f"This Robot Was Named As {robot2.name}, And His Type Was Defined As {robot2.type}.")