def onesAndzeroes(n):
    count0 = 0
    count1 = 0
    while n > 0:
        if n&1 == 0:
            count0 += 1
        elif n&1 == 1:
            count1 += 1

        n >>= 1
    return f"Total Ones = {count0}, And Total Zeroes = {count1}"

print(onesAndzeroes(int(input("Enter A Number: "))))