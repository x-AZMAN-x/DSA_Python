def binarySearch(arr, left, right, element):
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == element:
            return middle
        elif arr[middle] < element:
            left = middle + 1
        else:
            right = middle - 1
    return -1

arr = [5, 6, 7, 19, 41, 50, 75]
element = 41
result = binarySearch(arr, 0, len(arr) - 1, element)
if result != element:
    print(f"Element {element} Is Present At Index {result}.")
else:
    print(f"Element {element} Not Present In The Array.")