def longestConsicutiveOnes(num):
    count = 0
    max_count = 0
    while num > 0:
        if num & 1 == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
        n >>= 1
    return max_count

num = int(input("Enter A Number: "))
print(longestConsicutiveOnes(num))