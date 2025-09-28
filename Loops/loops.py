# Multiplication Table Using For Loop

num = int(input("Please Enter A Number You Want A Multiplication Table For: "))
for i in range(1,11,1):
    print(f"{num} X {i} = {num*i}")

#Square Pattern Using Stars With Nested For Loop

rows = 5

for i in range(1,rows+1):
    for o in range(1,rows+1):
        print(f"*", end = " ")
    print(" ")

# Sum Of All Natural Numbers
# Using For Loop

sum = 0
num = int(input("Please Enter A Number Till' You Want To Add Up To: "))

for i in range(1, num+1):
    sum += i

print(f"The Sum Of The First {num} Natural Numbers: {sum}.")

#While Loop

sum1 = 0
i = 1
while (i <= num):
    sum1 += i
    i += 1

print(f"The Sum Of The First {num} Natural Numbers: {sum1}.")
