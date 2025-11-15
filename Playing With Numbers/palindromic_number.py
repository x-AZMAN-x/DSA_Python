def is_palindrome(num):
    org_num = num
    rev = 0

    while (num > 0):
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    if (rev == org_num):
        return "Palindrome"
    else:
        return "Not Palindrome"

num = int(input("Enter A Number To Check If It Is A Palindromic Number Or Not: "))
print(f"The Number Is {is_palindrome(num)}.")