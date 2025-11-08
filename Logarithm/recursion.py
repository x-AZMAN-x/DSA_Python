# Space Complexity For Recursion

def sum_recursion(n):
    if n <= 0:
        return 0
    return(n + sum_recursion(n - 1))

num = int(input("Enter A Number: "))
print(sum_recursion(num))

print("Space Complexity = 0(n) Beacuse The Recursion Wil Be Iterated For num Time Where num Is The Input Number.")
