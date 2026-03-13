# 1) Create a function to sort 0s and 1s:
#    a) Take the list (A) and its size (n) as inputs.

# 2) Count how many 0s are present:
#    a) Initialize count = 0.
#    b) Loop through the list:
#       - If A[i] == 0, increase count.

# 3) Fill the array with 0s first:
#    a) Replace the first `count` positions with 0.
            
# 4) Fill the remaining positions with 1s:
#    a) From index `count` to n-1, set all values to 1.

# 5) Driver code:
#    a) Create a sample list A and find n using len(A).
#    b) Call sortZeroOne(A, n).
#    c) Print the sorted array.
def sortZeroOne(a, n):
    count = 0
    for i in range(0, n):
        if a[i] == 0:
            count += 1
    for i in range(count):
        a[i] = 0
    for i in range(count, n):
        a[i] = 1
    return a

a = [0, 0, 1, 1, 0, 1, 0]
n = len(a)
print(sortZeroOne(a, n))