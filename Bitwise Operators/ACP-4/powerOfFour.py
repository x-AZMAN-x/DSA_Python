def powerOfPower(number):
    powerValue = 0
    if (number & (number - 1) == 0):
        while (number > 1):
            number >>= 1
            powerValue += 1
        if (powerValue & 1 == 0):
            return True
        else:
            return False
        
number = int(input("Enter The Number You Want To Know If It Is A Power Of 4 Or Not: "))
print(powerOfPower(number))