def intersectionSort(arr1, arr2):
  res = []
  for i in range(len(arr2)):
    for j in range(len(arr1)):
      if arr1[i] == arr2[j]:
        res.append(arr2[j])
  return res
arr1 = [3, 4, 1, 6, 9, 6, 7, 2, 1]
arr2 = [5, 31, 21, 67, 41, 7, 6, 3]
print(intersectionSort(arr1, arr2))