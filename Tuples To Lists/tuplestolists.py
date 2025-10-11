my_tuple = (1, 3, 5, 7, 9, "Tuples", 3.3)
print(my_tuple)

my_tuple = 2, 4, 6, 8, "Tuples"
print(my_tuple)

tuple = ("Example",)

not_a_tuple = ("Example")

print(type(tuple))
print(type(not_a_tuple))

my_tuple = (11, 22, 33, 44, 55)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[len(my_tuple)-1])

print(my_tuple[1:3])
print(my_tuple[:4])
print(my_tuple[3:])
print(f"Every Alterantive Item Will Be Sliced: {my_tuple[::2]}")

print({f"Reversed Tuple: {my_tuple[::-1]}"})

tuple_1 = (2, 4, 6)
tuple_2 = ("x", "y", "z")
combined_tuple = tuple_1 + tuple_2

print(combined_tuple)

repeated_tuple = ("Tuples") * 3

print(repeated_tuple)

my_tuple = 1, 2, 3
my_tuple[0] = 10

nested_tuple = (2, 4, [6, 8])
print(nested_tuple[2][0])
nested_tuple[2][0] = 99
print(nested_tuple)