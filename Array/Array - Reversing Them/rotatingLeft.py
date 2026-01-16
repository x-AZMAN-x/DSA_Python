def rotatingLeft(arr, n):
    length = len(arr)
    if length == 0:
        return []
    
    n %= length
    if n == 0:
        return arr
    
    rotated = []
    rotated.extend(arr[n:])
    rotated.extend(arr[:n])

    return rotated
    
arr = list(map(int, input().split()))
n = int(input("Enter The Number: "))
print(rotatingLeft(arr, n))