def recursion():
    n = int(input("Enter A Number: "))
    print(n)
    if n < 0:
        return
    recursion()

print(recursion())