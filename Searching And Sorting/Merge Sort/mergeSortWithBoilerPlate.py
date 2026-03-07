# 1) Create a function for Merge Sort:
# a) Take a list (A) as input.
def mergeSort(arr):
# 2) Divide the list into two halves (if size > 1):
    if len(arr) > 1:
# a) Find mid = len(A) // 2.
        mid = len(arr) // 2
# b) Split into left = A[:mid] and right = A[mid:].
        left = arr[:mid]
        right = arr[mid:]
# 3) Recursively sort both halves:      
# a) Call mergeSorting(left).
        mergeSort(left)
# b) Call mergeSorting(right).
        mergeSort(right)
# 4) Merge the two sorted halves back into A:
# a) Use i to track left half index, j to track right half index.
        i = 0
        j = 0
# b) Use k to track the position in the main list A.
        k = 0
# 5) Compare and place smaller elements first:
# a) While i < len(left) and j < len(right):
        while i < len(left) and j < len(right):
# - If left[i] <= right[j], put left[i] into A[k] and increment i.
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
# - Else, put right[j] into A[k] and increment j.
            else:
                arr[k] = right[j]
                j += 1
# - Increment k after placing an element.
            k += 1
# 6) Copy any remaining elements:
# a) While i < len(left), copy left[i] into A[k] (increment i and k).
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
# b) While j < len(right), copy right[j] into A[k] (increment j and k).
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
# 7) Driver code:
# a) Create a sample list (A) and print it.
arr = [2, 5, 1, 0, 3, 8]
# b) Call mergeSorting(A) to sort it in-place.
mergeSort(arr)
# c) Print the sorted list.
print("Sorted List: {}".format(arr))