def heapify(arr, size, ind):
    """Fix At A Single Potential Violation At Index i, Assuming The Subtrees Rooted At Its Children Are Valid Max-Heaps. This Is The Core Operation - Insert, Extract And build_heap Are All Built On Top Of It."""
    largest = ind
    left = 2 * ind + 1
    right = 2 * ind + 2

    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right
    
    if largest == ind:
        print(f"Index {ind} (Value {arr[ind]} Already Beats Both Children) - STOP")
        return

    print(f"Index {ind} (Value{a[ind]} Loses To Index {largest}) Value{arr[largest]} - SWAP")
    arr[ind], arr[largest] = arr[largest], arr[ind]
    heapify(arr, size, largest)          # The Violation May Have Moved Further Down, Keep Going
    
arr = [90, 80, 70, 60, 50, 30, 20, 10]
size = len(arr)
print("Array Before: ", arr)
heapify(arr, size, 0)
print("Array After: ", arr)