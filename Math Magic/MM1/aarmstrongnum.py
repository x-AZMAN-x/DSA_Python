num = int(input("Enter A Number To Check Whether It Is A Armstrong Number Or Not: "))
len_of_num = len(str(num))
a_num = 0
x = num

while (x > 0):
    digit = x % 10
    a_num += digit ** len_of_num
    x //= 10

print(f"{num} Is An Armstrong Number.") if num == a_num else print(f"{num} Is Not An Armstrong Number.")
