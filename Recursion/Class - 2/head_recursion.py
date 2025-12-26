def headRecursion(n, num):
    if n > num:
        return
    headRecursion(n+1, num)
    print(n)

n, num = map(int, input("Enter Two Numbers With A Space: ").split())
print(headRecursion(n, num))