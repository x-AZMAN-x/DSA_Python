def meanMedian(arr):
    if len(arr) == 0:
        return None, None 
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    mean = sum//len(arr)
    sorted_array = sorted(arr)
    if len(arr)%2 == 1:
        median = arr[len(arr)//2]
    else:
        mid1 = arr[len(arr)//2 - 1]
        mid2 = arr[len(arr)//2]
        median = mid1 + mid2 /2
    return mean, median

array = [23, 64, 67, 41, 69, 21]
print(meanMedian(array))