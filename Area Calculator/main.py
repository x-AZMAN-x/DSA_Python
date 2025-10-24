class Polygon:
    def __init__(self, name):
        self.name = name

    def calculate_area(self):
        pass

class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height
    
class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width
    
class Circle(Polygon):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2
    
print("Polygons Calculating...")

triangle = Triangle(10, 5)
rectangle = Rectangle(8, 6)
circle = Circle(7)

shapes = [triangle, rectangle, circle]

for shape in shapes:
    area = shape.calculator_area()
    print(f"{shape.name} Area: {area:.2f}")