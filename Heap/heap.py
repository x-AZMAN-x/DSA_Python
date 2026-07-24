def isValidMaxHeap(arr):
    size = len(arr)
    for i in range(size):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < size and arr[i] < arr[left]:
            return False
        if right < size and arr[i] < arr[right]:
            return False
    return True

good = [90, 80, 70, 50, 45, 60, 10, 20, 15, 30, 25]
bad = [90, 80, 70, 50, 45, 60, 10, 20, 15, 99, 25]          # 99 Breaks The Rule At Index 9 (parent 45 < 99)

print("Is This Array A Valid Max Heap?", isValidMaxHeap(good))          # Returns True
print("Is This Array A Valid Max Heap?", isValidMaxHeap(bad))          # Returns False