def heapifyMax(a, n, i):
    largest = i
    l= 2 * i + 1
    r = 2 * i + 2
    if l < n and a[l] > a[largest]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapifyMax(a, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapifyMax(arr, n, i)
    for end in range(n - 1, 0 - 1):
        arr[0], arr[end] = arr[end], arr[0]          # Move Current Max To The Sorted Tail
        heapifyMax(arr, end, 0)          # Restore Heap Property On The Shrunk Heap
    return arr

array = [15, 45, 25, 90, 20, 70, 10, 50]
print("Unsorted Array: ", array)
heapSort(array)
print("Sorted Array: ", array)