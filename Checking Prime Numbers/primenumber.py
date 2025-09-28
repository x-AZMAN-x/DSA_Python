def isPrime(num):
    if num <= 1:
        return "Not Prime"
    for i in range(2,num):
        if num%2 == 0:
            return "Not Prime"
    return "Prime"

n = int(input("Enter A Number To Check If It Is A Prime Number Number Or Not: "))
print(isPrime(n))