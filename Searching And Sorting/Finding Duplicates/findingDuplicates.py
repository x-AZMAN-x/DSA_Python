def find_duplicate_with_sort(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            return arr[i]
    return None

arr = [1, 2, 3, 4, 4, 5]
duplicate = find_duplicate_with_sort(arr)
print(f"The duplicated integer is: {duplicate}")