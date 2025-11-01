def bigO_n(n):
    iteration = 0
    sum = 0
    
    for i in range(1, n+1):
        iteration += 1
        sum += 1

    print(f"When n = {n}, The Sum = {sum}, And The Time Complexity = 0(n).")

bigO_n(2)
bigO_n(3)
bigO_n(4)
bigO_n(500)
bigO_n(5000)
bigO_n(50000000)
