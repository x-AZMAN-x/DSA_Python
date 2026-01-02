def reversedNum(num, newReversedNum = 0):
    if num < 0:
        return -reversedNum(abs(num))
    if num == 0:
        return newReversedNum
    
    last_digit = num % 10
    newReversedNum = newReversedNum * 10 + last_digit
    return reversedNum(num // 10, newReversedNum)

num = int(input("Enter Your Number: "))
print(reversedNum(num))