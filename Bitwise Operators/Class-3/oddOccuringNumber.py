def oddOccuringNumber(arr):
    xor = 0
    for num in arr:
        xor ^= num
    return xor

arr = []  #Blank Array
size_arr = int(input("Enter The Size Of The Array: "))  #Odd Size

while (size_arr > 0):
    num = int(input("Enter A Number For The List: "))
    arr.append(num)
    size_arr -= 1

res = oddOccuringNumber(arr)
print(res)