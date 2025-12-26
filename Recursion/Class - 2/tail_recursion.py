def tailRecursion(n, num):
    if n > num:
        return
    print(n)
    tailRecursion(n+1, num)

n, num = map(int, input("Enter Two Numbers With A Space: ").split())
print(tailRecursion(n, num))