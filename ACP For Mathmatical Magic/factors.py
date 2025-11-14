num = int(input("Enter A Number To Find Its Factor: "))
factors = []
for i in range(1, num // 2 + 1):
    if num % i == 0:
        factors.append(i)

print(factors)