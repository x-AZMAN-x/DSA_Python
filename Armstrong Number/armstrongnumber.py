def armstrongNumber(num):
    temp_num = num
    armstrong_num = 0
    while(temp_num > 0):
        last_digit = temp_num%10 #Extracting The Last Digit
        armstrong_num += last_digit**len(str(num))
        temp_num//=10 #Finding The Remaining Number Except The Last Digit
    
    if armstrong_num == num:
        return "Armstrong Number"
    else:
        return "Not An Armstrong Number"
    
    
n = int(input("Enter a Number: "))   
print(armstrongNumber(n))