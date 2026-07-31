def heapify(a, n, i):
    """Fix At A Single Potential Violation At Index i, Assuming The Subtrees Rooted At Its Children Are Valid Max-Heaps. This Is The Core Operation - Insert, Extract And build_heap Are All Built On Top Of It."""
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and a[l] > a[largest]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r
    
    if largest == i:
        print(f"Index {i} (Value {a[i]} Alreadt Beats Both Children) - STOP")
        return

    print(f"Index {i} (Value{a[i]} Loses To Index {largest}) Value{a[largest]} - SWAP")
    a[i], a[largest] = a[largest], a[i]
    heapify(a, n, largest)          # The Violation May Have Moved Further Down, Keep Going
    
a = [10, 90, 80, 70, 60, 50, 40, 30, 20]
n = len(a)
print("Array Before: ", a)
heapify(a, n, 0)
print("Array After: ", a)