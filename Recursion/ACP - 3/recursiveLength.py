def recursiveLength(arr):
    if not arr:
        return 0
    return 1 + recursiveLength(arr[1:])

my_list = [40, 69, 19, 67, 41]
print(f"Length of {my_list}: {recursiveLength(my_list)}")