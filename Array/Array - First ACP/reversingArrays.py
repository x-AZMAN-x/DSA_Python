def reversingArrays(arr):
    reverse = []
    for i in range(len(arr)-1, -1, -1):
        reverse.append(arr[i])
    return reverse

array = [21, 67, 69, 41, 95]
print(reversingArrays(array))