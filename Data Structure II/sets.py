#Creating A Set
fruits = {"Orange", "Lichie", "Banana"}
print(fruits)

hetergenous_set = {"Sets", 3.3, 67}
print(hetergenous_set)

numbers = set([1, 3, 5, 7, 9])
print(list(numbers))

not_an_empty_list = {}
empty_list = set()
print(empty_list)

#Adding Elements
my_set = {2, 4, 6}
my_set.add(8)
print(my_set)
my_set.update([0])
print(f"Updated Set: {my_set}")

my_set = {1, 3, 5, 7, 9}

my_set.remove(7)
print(my_set)

my_set.discard(10)
print(my_set)
    
popped = my_set.pop()
print(f"Popped Element: {popped}")

print(f"Popped Set: {my_set}")
my_set.clear()
print(my_set)

#Set Of Operations
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

#Or
print(f"Union Of Set: {A | B}")
#And
print(f"Intersection Of Set: {A & B}")
#Subtract(A To B)
print(f"Difference From A To B: {A - B}")
#Subtract(B To A)
print(f"Difference From B To A: {B - A}")
#Power
print(f"Symmetric Difference Between Sets: {A ^ B}")