def shellSort(arr, size):
    gap = size//2

    while gap > 0:
        for i in range(gap, size):
            tempo = arr[i]
            j = i

            while j >= gap and arr[j - gap] > tempo:
                arr[j] = arr[j - gap]
                j -= gap
                arr[j] = tempo
            arr[j] = tempo
        gap //= 2
    return arr

arr = [3, 9, 5, 1, 2, 4, 6, 7]
size = len(arr)
print(shellSort(arr, size))

#Largest Element Of The Array
print(arr[-1])