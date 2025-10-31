import time
def linearTime(n):
    iteration = 0
    sum = 0
    start = time.time()
    for i in range(1, n+1):
        iteration += 1
        sum += 1
    
    end = time.time()
    print(f"When n = {n}, The Sum = {sum} And The Number Of Iteration = {iteration} And Time Taken = {end - start}")

linearTime(2)
linearTime(3)
linearTime(4)
linearTime(10)
linearTime(500)
linearTime(5000)
linearTime(5000000)