# #Greeting

# def greeting(name, msg):
#     output = f"Hi {msg}, I Am {name}."
#     return output

# f_name = input("Please Enter Your Name: ")
# greet = input("Enter Your Wish: ")

# input = greeting(f_name, greet)
# print(input)

#Calculator

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

def calculator(a, b):
    operator = input("Enter The Operator(+, -, *, /): ")
    if operator == "+":
        print(add(a, b))
    elif operator == "-":
        print(subtract(a, b))
    elif operator == "*":
        print(multiply(a, b))
    elif operator == "/":
        print(divide(a, b))
    else:
        print("Please Enter A Valid Operator.")

num_1 = int(input("Please Enter A Number: "))
num_2 = int(input("Please Enter Another Number: "))

calculator(num_1, num_2)