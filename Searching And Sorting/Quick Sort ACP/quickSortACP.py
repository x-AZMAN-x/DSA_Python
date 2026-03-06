def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[high], arr[i + 1] = arr[i + 1], arr[high]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)
        return arr
    
arr = [2, 9, 10, 3, 7, 6, 1, 8, 4, 5]
print(quickSort(arr, 0, len(arr) - 1))