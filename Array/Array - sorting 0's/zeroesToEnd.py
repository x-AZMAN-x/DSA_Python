def movingZeroesToEnd(a, a_size):
    zero = 0
    non_zero = 0

    while (non_zero != a_size):
        if a [non_zero] != 0:
            a[non_zero], a[zero] = a[zero], a [non_zero]
            zero += 1
        non_zero += 1

a = [1, 0, 3, 6, 0, 0, 0, 2, 355, 0, 72]
a_size = len(a)
print("Array Now: ")
print(a)
movingZeroesToEnd(a, a_size)
print("Array After Pushing Zeroes To End: ")
print(a)