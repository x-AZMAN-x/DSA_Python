def kadaneAlgorithm(array, size):
    maxSum = array[0]
    res = array[0]
    for i in range(1, size):
        maxSum = max(maxSum + array[i], array[i])
        res = max(res, maxSum)
    return res

array = list(map(int, input("Enter An Array: ").split()))
size = len(array)
print(kadaneAlgorithm(array, size))