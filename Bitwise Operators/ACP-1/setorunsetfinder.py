def setBitOrUnsetBit(n, pos):
    if (n & (1 << pos - 1)):
        return "Set Bit"
    else:
        return "Unset Bit"
    
res = setBitOrUnsetBit(int(input("Enter A Number: ")), int(input("Enter A Position: ")))
print(res)