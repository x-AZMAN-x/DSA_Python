class PerimeterCalculator:
    def square(self, side):
        self.side = side

        side = int(input("Enter The Side For The Square: "))
        perimeter = print(f"The Perimeter For Square Is: {side + side + side + side}.")
        print(perimeter)

    def rectangle(self, height, width):
        height = int(input("Enter The Height Of The Rectangle: "))
        width = int(input("Enter The Width Of The Rectangle: "))
        perimeter = print(f"The Perimeter For The Rectangle: {height + height + width + width}.")
        print(perimeter)
    
    def triangle(self, side1, side2, side3):
        side1 = int(input("Enter The Height Of The Rectangle: "))
        side2 = int(input("Enter The Width Of The Rectangle: "))
        side3 = int(input("Enter The Width Of The Rectangle: "))
        perimeter = print(f"The Perimeter For The Rectangle: {side1 + side2 + side3}.")
        print(perimeter)

    def choices(one, two, three):
        one = 1
        two = 2
        three = 3
        print("Welcome To The Perimeter Calculator! Please Choose Which Shape You Want To Find The Perimeter For:-\n1. Square\n2. Rectangle\n3. Triangle")
        choice = int(input("Enter Your Choice:- "))
        if choice == one:
            PerimeterCalculator.square()
        if choice == two:
            PerimeterCalculator.rectangle()
        if choice == three:
            PerimeterCalculator.triangle()

PerimeterCalculator.choices()