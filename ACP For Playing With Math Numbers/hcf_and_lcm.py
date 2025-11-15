def hcf(a, b):
    while b > 0:
        a, b = a, b % b
    return a

n1 = int(input("Enter The First Number: "))
n2 = int(input("Enter The Second Number: "))

print(f"HCF Of {n1} And {n2} Is {hcf(n1, n2)}.")

lcm = n1 * n2 / hcf(n1, n2)
print(f"LCM Of {n1} And {n2} Is {lcm}.")