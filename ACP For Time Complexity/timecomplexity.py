# Linear

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

# Expotential

import time
def linearTime(n):
    iteration = 0
    sum = 0
    start = time.time()
    for i in range(1, n+1):
        for j in range(1, n+1):
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

# Constant
import time
def sum_number(n):
    iteration = 0
    print(f"The Sum Upto Number EnteredBy The User: ")
    start = time.time()
    sum = n*(n+1)/2  # Formula
    end = time.time()
    iteration += 1

    print(f"Total Number Of Iteration Is = {iteration} And The Sum Is {sum} And The Time Taken Is {end - start}")

sum_number(5)
sum_number(200)
sum_number(50000000)
