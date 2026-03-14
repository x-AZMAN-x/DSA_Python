def generalSort(arr, size):
    count = 0
    for i in range(1, size):
        if (arr[i-1] > arr[1]):
            count += 1

    if (arr[size-1] > arr[0]):
            count += 1
    return (count <= 1)

arr = [1, 2, 3, 5, 4]
size = len(arr)
print(generalSort(arr, size))