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
    
arr = [5, 2, 9, -3, 4, 6, 7, 1, 5]
print(quickSort(arr, 0, len(arr) - 1))

# Time Complexity = O(n log n)
# Space Complexity = O(n)