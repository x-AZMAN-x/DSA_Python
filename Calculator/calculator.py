import math
from fractions import Fraction

def cont():
    conti = input("Do You Want To Continue Using The Calculator? (1. Yes, 2. No) - ")
    if conti == "Yes" or conti == "yes" or conti == "1":
        simpleCalculator()
    elif conti == "No" or conti == "no" or conti == "2":
        print("Thank You For Using This Calculator.")
    else:
        print("Not A Valid Option! Choose A Valid One.")

def contin(result):
    conti = input("Do You Want To Continue? (1.Yes, 2.No): ")

    if conti == "Yes" or conti == "yes" or conti == "1":
        scientificCalculator(result)
    elif conti == "No" or conti == "no" or conti == "2":
        print("Thank You For Using This Calculator.")

def conversion(res):
    convert = input("Do You Want To Convert Your Answer To Fraction? (1. Yes, 2. No) - ")
    if convert == "Yes" or convert == "yes" or convert == "1":
        convertedAns = Fraction(res).limit_denominator()
        print("The Converted Answer Is", convertedAns)
    elif convert == "No" or convert == "no" or convert == "2":
        print()
    else:
        print("Not An Option! Choose A Valid One.")
        conversion(res)

def simpleCalculator():
    action = input("What Do You Want To Do?(1. Add, 2. Subtract, 3. Multiply, 4. Divide) - ")
    
    if action == "Add" or action == "add" or action == "1":
        num1 = int(input("Enter The First Number You Want To Add: "))
        num2 = int(input("Enter The Second Number You Want To Add: "))
        add(num1, num2)
    elif action == "Subtract" or action == "subtract" or action == "2":
        num1 = int(input("Enter The First Number You Want To Subtract: "))
        num2 = int(input("Enter The Second Number You Want To Subtract: "))
        sub(num1, num2)
    elif action == "Multiply" or action == "multiply" or action == "3":
        num1 = int(input("Enter The First Number You Want To Multiply: "))
        num2 = int(input("Enter The Second Number You Want To Multiply: "))
        multi(num1, num2)
    elif action == "Divide" or action == "divide" or action == "4":
        num1 = int(input("Enter The First Number You Want To Divide: "))
        num2 = int(input("Enter The Second Number You Want To Divide: "))
        div(num1, num2)
    else:
        print("Not An Available Action! Please Type An Action That Is Possible To Do.")
        simpleCalculator()

def scientificCalculator(result):
    action = input("What Do You Want To Do?(1. Add, 2. Subtract, 3. Multiply, 4. Divide, 5. Power, 6. Square Root, 7. Cube Root, 8. Previous Answer, 9. Sin, 10. Cos, 11. Tan, 12. Log) - ")
    if action == "Add" or action == "add" or action == "1":
        num1 = int(input("Enter The First Number You Want To Add: "))
        num2 = int(input("Enter The Second Number You Want To Add: "))
        addition(num1, num2)
    elif action == "Subtract" or action == "subtract" or action == "2":
        num1 = int(input("Enter The First Number You Want To Subtract: "))
        num2 = int(input("Enter The Second Number You Want To Subtract: "))
        subtraction(num1, num2)
    elif action == "Multiply" or action == "multiply" or action == "3":
        num1 = int(input("Enter The First Number You Want To Multiply: "))
        num2 = int(input("Enter The Second Number You Want To Multiply: "))
        multiply(num1, num2)
    elif action == "Divide" or action == "divide" or action == "4":
        num1 = int(input("Enter The First Number You Want To Divide: "))
        num2 = int(input("Enter The Second Number You Want To Divide: "))
        divide(num1, num2)
    elif action == "Power" or action == "power" or action == "5":
        num = int(input("Enter The Number: "))
        pow = int(input("Enter The Power: "))
        powr(num, pow)
    elif action == "Square Root" or action == "Square root" or action == "square root" or action == "6":
        number = int(input("Enter The Number You Want To Square Root: "))
        squareRoot(number)
    elif action == "Cube Root" or action == "Cube root" or action == "cube root" or action == "7":
        numb = int(input("Enter The Number You Want To Cube Root: "))
        cubeRoot(numb)
    elif action == "Sin" or action == "sin" or action == "9":
        n = int(input("Enter The Number You Want To Find The Sin Of: "))
        sin(n)
    elif action == "Cos" or action == "cos" or action == "10":
        n = int(input("Enter The Number You Want To Find The Cos Of: "))
        cos(n)
    elif action == "Tan" or action == "tan" or action == "11":
        n = int(input("Enter The Number You Want To Find The Tan Of: "))
        tan(n)
    elif action == "Log" or action == "log" or action == "12":
        n = int(input("Enter The Number You Want To Find The Log Of: "))
        log(n)
    elif action == "Previous Answer" or action == "Previous answer" or action == "previous answer" or action == "8":
        print("The Previous Answer Was:", result)
        contin(result)
    else:
        print("Not An Available Action! Please Type An Action That Is Possible To Do.")
        scientificCalculator(0)

def add(n1, n2):
    res =  n1 + n2
    print(f"{n1} + {n2} = {res}")
    cont()

def sub(n1, n2):
    res =  n1 - n2
    print(f"{n1} - {n2} = {res}")
    cont()

def multi(n1, n2):
    res =  n1 * n2
    print(f"{n1} * {n2} = {res}")
    conversion(res)
    cont()

def div(n1, n2):
    res =  n1 / n2
    print(f"{n1} / {n2} = {res}")
    cont()

def addition(n1, n2):
    res = n1 + n2
    print(f"{n1} + {n2} = {res}")
    conversion(res)
    contin(res)

def subtraction(n1, n2):
    res =  n1 - n2
    print(f"{n1} - {n2} = {res}")
    conversion(res)
    contin(res)

def multiply(n1, n2):
    res =  n1 * n2
    print(f"{n1} * {n2} = {res}")
    conversion(res)
    contin(res)

def divide(n1, n2):
    res =  n1 / n2
    print(f"{n1} / {n2} = {res}")
    conversion(res)
    contin(res)

def powr(num, pow):
    res = num ** pow
    print(f"{num} ^ {pow} = {res}")
    conversion(res)
    contin(res)

def squareRoot(num):
    res = math.sqrt(num)
    print(f"The Square Root Of {num} Is {res}")
    conversion(res)
    contin(res)

def cubeRoot(num):
    res = math.cbrt(num)
    print(f"The Cube Root Of {num} Is {res}")
    conversion(res)
    contin(res)

def sin(num):
    res = math.sin(num)
    print(f"The Sin Of {num} Is {res}")
    conversion(res)
    contin(res)

def cos(num):
    res = math.cos(num)
    print(f"The Cos Of {num} Is {res}")
    conversion(res)
    contin(res)

def tan(num):
    res = math.tan(num)
    print(f"The Tan Of {num} Is {res}")
    conversion(res)
    contin(res)

def log(num):
    res = math.log(num)
    print(f"The Log Of {num} Is {res}")
    conversion(res)
    contin(res)

def calculator():
    calc = input("Which Calculator Do You Want To Use?(1. Simple Calculator, 2. Scientific Calculator) - ")

    if calc == "Simple Calculator" or calc == "Simple calculator" or calc == "simple calculator" or calc == "Simple" or calc == "simple" or calc == "1":
        simpleCalculator()
    elif calc == "Scientific Calculator" or calc == "Scientific calculator" or calc == "scientific calculator" or calc == "Scientific" or calc == "scientific" or calc == "2":
        scientificCalculator(0)
    else:
        print("Not A Type Of Calculator! Please Type One That Is A Type Of Calculator.")
        calculator()

calculator()