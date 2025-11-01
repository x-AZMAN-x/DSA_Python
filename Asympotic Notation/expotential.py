def bigO_n2(n):
    iteration = 0
    sum = 0
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            iteration += 1
            sum += 1

    print(f"When n = {n}, The Sum = {sum}, And The Time Complexity = 0(n^2).")

bigO_n2(2)
bigO_n2(3)
bigO_n2(4)
bigO_n2(500)
bigO_n2(5000)
bigO_n2(50000000)
