
def sortingArrays(arr):
    size = len(arr)

    for i in range(size):
        for o in range(0, size - i - 1):
            if arr[o] > arr[o + 1]:
                arr[o], arr[o + 1] = arr[o + 1], arr[o]
    return arr

# Example usage:
my_array = [1, 5, 23, 0, 0, 0, 34, 67, 0]
sorted_array = sortingArrays(my_array)
print(f"Sorted array: {sorted_array}")