def isPrime(n):
    if n >= 1:
        for i in range(2, n // 2 + 1):
            if n%i == 0:
                return "Not Prime"
        return "Prime"
    else:
        return "Not Prime"
    
n = int(input("Enter A Number To Check If It Is A Prime Number Or Not: "))
print(f"{isPrime(n)}")