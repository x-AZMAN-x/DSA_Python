def print1to10(n):
    if (n > 10):
        return
    print(n)
    print1to10(n + 1)

print(print1to10(int(input("Enter A Number: "))))