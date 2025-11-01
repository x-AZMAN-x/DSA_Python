def bigO_one(n):
    iteration = 0
    print(f"The Sum Upto The Number Entered By The User Is: ")
    sum = n*(n+1)/2 # Formula
    iteration += 1

    print(f"Total Number Of Iteration Is {iteration}, And The Sum Is {sum}, And The Time Complexity = O(1).")

bigO_one(5)
bigO_one(200)
bigO_one(50000000)
