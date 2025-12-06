def reverse_bits(num):
    res = 0
    bits = num.bit_length()
    
    for i in range(bits):
        bit = num & 1
        result = (result << 1) | bit
        num >>= 1
    return result

num = int(input("Enter A Number: "))
reversed_num = reverse_bits(num)

print(f"Original Number = {num}")
print(f"Reversed Bits Number = {reversed_num}")