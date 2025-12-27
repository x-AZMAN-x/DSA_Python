def maxRecursive(arr):
    size = len(arr)
    if size == 1:
        return arr[0]
    return max(arr[0], maxRecursive(arr[1:]))

array = [10, 50, 37, 67, 49]
print(maxRecursive(array))