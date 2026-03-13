def insertionSort(arr, size):
  for i in range(1, size):
    curr = arr[i]
    j = i - 1
    while j >= 0 and curr < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = curr
  return arr

arr = [3, 4, 1, 6, 9, 6, 7, 2, 1]
size = len(arr)
print(insertionSort(arr, size))