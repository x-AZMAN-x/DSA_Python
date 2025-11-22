def sieveOfEratosthenes(n):
    if n < 2:
        return []
    
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i,n + 1, i):
                is_prime[j] = False

    primes = [i for i, prime in enumerate(is_prime) if prime == True]
    return primes

print(sieveOfEratosthenes(10))
print("Time Complexity For This Algorithm Is 0(nlog(n)) And Space Complexity Is 0(n).")