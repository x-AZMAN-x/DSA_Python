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