#Creating A Tuple
#Using Parenthesis
my_tuple = (1, 3, 5, 7, 9, "Tuples", 3.3)
print(my_tuple)

#Without Using Parenthesis
my_tuple = 2, 4, 6, 8, "Tuples"
print(my_tuple)

#How Can We Create Tuples
tuple = ("Example",) # (Requires A Comma)

not_a_tuple = ("Example") # (Output Will Show As 'str')

print(type(tuple))
print(type(not_a_tuple))

# #Tuples From Lists
# tuple_from_list = tuple([1, 2, 3, 4, 5], )
# print(tuple_from_list)

#Accessing Tuple Elements
my_tuple = (11, 22, 33, 44, 55)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[len(my_tuple)-1])

#Slicing A Tuple
print(my_tuple[1:3])
print(my_tuple[:4])
print(my_tuple[3:])
print(f"Every Alterantive Item Will Be Sliced: {my_tuple[::2]}")

#Reversing The Tuple
print({f"Reversed Tuple: {my_tuple[::-1]}"})

#Tuple Operations
#Addition
tuple_1 = (2, 4, 6)
tuple_2 = ("x", "y", "z")
combined_tuple = tuple_1 + tuple_2

print(combined_tuple)

#Multiplication
repeated_tuple = ("Tuples") * 3

print(repeated_tuple)

my_tuple = 1, 2, 3
my_tuple[0] = 10 #ERROR: 'tuple' Object Does Not Support Item Assignment

nested_tuple = (2, 4, [6, 8])
print(nested_tuple[2][0])
nested_tuple[2][0] = 99
print(nested_tuple)
