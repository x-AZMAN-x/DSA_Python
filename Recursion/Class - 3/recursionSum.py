def recursionSum(arr, index = 0):
    if index == len(arr):
        return 0
    return arr[index] + recursionSum(arr, index + 1)

arrays = [
    [10, 30, 25, 90],
    [7, 3, 6, 7],
    [15, 25, 19],
    [],
    [67],
]

for arr in arrays:
    sum = recursionSum(arr)
    print(f"Array: {arr}")
    print(f"Sum With Index: {sum}")
    print()