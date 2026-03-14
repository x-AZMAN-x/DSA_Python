def rotatedArr(arr, r):
    r = r%len(arr)
    res = arr[r:]+arr[:r]
    return res

arr = [1, 3, 5, 6, 7, 0]
r = int(input("Enter How Many Times You Want To Rotate: "))
print(rotatedArr(arr, r))