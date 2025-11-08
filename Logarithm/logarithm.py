def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iteration = 0
    while left <= right:
        iteration += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return f"Element {mid} Is Found With Iterations, {iteration}!"
        elif arr[mid] < target:
            left = mid +1
        else:
            right = mid - 1
    
    return f"Element {target} Can Not Be Found With Iterations, {iteration}..." 
    
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 5

print(binary_search(numbers, target))
