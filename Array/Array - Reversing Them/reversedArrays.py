def reverseInGroups(arr, n):
    length = len(arr)
    for i in range(0, length,n):
        left = i
        right = min(i + n - 1, length - 1)
        
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

arr = list(map(int, input().split()))
n = int(input("Enter The Number: "))
print(reverseInGroups(arr, n))