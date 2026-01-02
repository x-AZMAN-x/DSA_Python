def powerOfTwo(num):
    while (num != 1):
        if num % 2 != 0:
            return False
    return powerOfTwo(num // 2)

print(powerOfTwo(int(input("Enter A Number: "))))