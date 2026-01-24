def maxCircularSum(array):
    totalSum = 0
    maximum = array[0]
    minimum = array[0]
    currentMax = 0
    currentMin = 0
    for i in array:
        totalSum += i
        currentMax = max(currentMax + i, i)
        maximum = max(maximum, currentMax)
        currentMax = min(currentMin + i, i)
        minimum = min(minimum, currentMin)
    
    if minimum == totalSum:
        return maximum
    
    return max(maximum, totalSum - minimum)

array = list(map(int, input("Enter An Array: ").split()))
print(maxCircularSum(array))