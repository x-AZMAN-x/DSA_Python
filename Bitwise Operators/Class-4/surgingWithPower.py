def isPowerTwoOrNot(n):
    if n <= 0:
        return False
    return (n & (n-1) == 0)
 
num= int(input("Enter A Number To Check If It Is A Power OF 2 Or Not: "))
print(isPowerTwoOrNot(num))