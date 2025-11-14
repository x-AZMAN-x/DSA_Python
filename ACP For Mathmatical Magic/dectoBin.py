decimal_num = int(input())
binary_result = ""

if decimal_num == 0:
    binary_result == "0"
else:
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_result = str(remainder) + binary_result
        decimal_num = decimal_num // 2

print(binary_result)