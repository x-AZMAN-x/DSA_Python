def powerOfTwo(num):
    while (num != 1):
        if num % 2 != 0:
            return False
        num //= 2

    return True

print(powerOfTwo(int(input("Enter A Number: "))))