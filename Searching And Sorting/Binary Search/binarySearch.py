def binarySearch(arr, l, r, x):
    while l <= r:
        mid = (l + r) // 2
        #Checking If x Is Present At mid
        if arr[mid] == x:
            return mid
        #If x Is Greater, Ignore The Left Side
        elif arr[mid] < x:
            l = mid + 1
        #If x Is Smaller, Ignore The Right Side
        else:
            r = mid - 1
    #Return -1 If The Element Is Not Found In The Array
    return -1

#Driver Code
arr = [2, 3, 4, 10, 40]
x = 10
result = binarySearch(arr, 0, len(arr) - 1, x)
if result != x:
    print(f"Element {x} Is Present At Index {result}.")
else:
    print(f"Element {x} Not Present In The Array.")