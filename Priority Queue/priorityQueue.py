import heapq
# heapq Only Gives You A Min-Heap Built On Top Of A Plain List
arr = [50, 30, 70, 20, 40, 60, 80]
heapq.heapify(arr)          # Rearrange The List In Place O(n)
print("Heapified: ", arr)

heapq.heappush(arr, 5)
print("After heappush(5): ", arr)

smallest = heapq.heappop(arr)
print("heappop() => ", smallest, "Remaining: ", arr)

print("3 Smallest: ", heapq.nsmallest(3, arr))
print("3 Largest: ", heapq.nlargest(3, arr))

# Trick For A Max - Heap: Negate Values Going In, Negate Again Coming Out
max_heap = []
for v in [50, 30, 70, 20, 90]:
    heapq.heappush(max_heap, -v)
print("\nMax-Heap Internal Storage (Negated): ", max_heap)
print("Largest Value: ", -max_heap[0])  