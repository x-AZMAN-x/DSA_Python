def maxConsecutiveOnes(array, size):
    count = 0
    maxCount = 0
    for i in range(size):
        if array[i] != 1:
            count = 0
        else:
            count += 1
            maxCount = max(count, maxCount)
    return maxCount
    
array = [1, 2, 4, 1, 1, 1, 1]
size = len(array)
print(maxConsecutiveOnes(array, size))