def linearSearch(arr, x):
    size = len(arr)
    for i in range(0, size):
        if x == arr[i]:
            return i
    return -1
    
arr = [3, 7, 6, 9, 3, 1, 4, 8]
print(linearSearch(arr, 1))