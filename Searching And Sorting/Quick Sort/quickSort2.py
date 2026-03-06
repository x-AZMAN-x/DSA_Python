def quickSort(book_list):
    if len(book_list) <= 1:
        return book_list
    
    pivot = book_list[0]
    small = [b for b in book_list[1:] if b < pivot]
    large = [b for b in book_list[1:] if b >= pivot]

    return quickSort(small) + [pivot] + quickSort(large)

arr = [5, 2, 9, -3, 4, 6, 7, 1, 5]
print(quickSort(arr))

# Time Complexity = O(n log n)
# Space Complexity = O(3n)