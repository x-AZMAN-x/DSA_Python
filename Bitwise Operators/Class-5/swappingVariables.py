# Swapping Variables Normally(Without Bitwise)
def swappingVariablesWithoutBitwise(num1, num2):
    print(num1, num2)
    temp_variable = num1 
    num1 = num2
    num2 = temp_variable
    print("Swapping The Variables...")
    return num1, num2

num1 = int(input("Enter The First Number: "))
num2 = int(input("Enter The Second Number: "))
# print(swappingVariablesWithoutBitwise(num1, num2))

# Swapping Variables Using Bitwise
def swappingVariablesWithBitwise(num1, num2):
    print(num1, num2)
    num1 = num1 ^ num2
    num2 = num1 ^ num2
    num1 = num1 ^ num2
    print("Swapping Variables...")
    return num1, num2

print(swappingVariablesWithBitwise(num1, num2))