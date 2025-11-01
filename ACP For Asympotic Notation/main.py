# Constant
def bigO_one(n):
    iteration = 0
    print(f"The Sum Upto The Number Entered By The User Is: ")
    sum = n*(n+1)/2 # Formula
    iteration += 1

    print(f"Total Number Of Iteration Is {iteration}, And The Sum Is {sum}, And The Time Complexity = O(1).")

bigO_one(5)
bigO_one(200)
bigO_one(50000000)

# Linear
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

# Expotential
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
