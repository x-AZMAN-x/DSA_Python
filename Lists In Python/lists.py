lst = ["Apple", "Orange", "Mango", "Lichie", "Banana", "Carrot"]

print(f"First Element Of The List: {lst[0]}")
print(f"Last Element OF The List: {lst[len(lst)-1]}")
print(f"Last Element of The List: {lst[-1]}")
print(f"Second Last Element Of The List: {lst[len(lst)-2]}")

lst.append("Malta")
print(f"Updated List:", lst)

lst.remove("Apple")
print("Updated List:", lst)

lst.sort()
print("Sorted List In Alphabetical Order:", lst)

lst.pop(4)
print("Updated List:", lst)

lst.reverse()
print("Reversed List In Alphabetical Order:", lst)

print("Multiplied List:", lst*2)

lst = lst[2:3]
print("Sliced List:", lst)

reversed_list = lst[::-1]
print("Reversed List:", reversed_list)

lst.clear()
print("Updated List:", lst)