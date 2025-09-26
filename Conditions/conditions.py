# Finding Your BMI
weight = float(input("Please Enter Your Weight In kg: "))
height = float(input("Please Enter Your Height In Meters: "))

bmi = weight/(height ** 2)

if bmi < 18.5:
    category ="Underweight"
elif bmi < 25:
    category = "Normal Weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI Is {bmi:.1f} ({category}).")

#Finding Whether A Number Is Odd Or Even
num = int(input("Please Enter A Number To Check Wheter It Is Odd Or Even: "))
#Traditional Way
if num %2 == 1:
    print("The Number Is Odd.")
else:
    print("The Number Is Even.")

# #Ternary Operator
odd_even = f"The Number Is Odd." if (num %2 == 1) else f"The Number Is Even."
print (odd_even)

#Nested Conditionals
num = int(input("Please Enter A Number: "))

if num > 10:
    print(f"{num} Is Greater Than 10.")
    if num > 20:
        print(f"{num} Is Greater Than 20.")
        if num > 30:
            print(f"{num} Is Greater Than 30.")
        else:
            print(f"{num} Is Less Than 30.")
    else:
        print(f"{num} Is Less Than 20.")
else:
    print(f"{num} Is Less Than 10.")        