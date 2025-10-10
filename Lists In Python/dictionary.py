my_dict = {}
my_dict = {
    1 : "Azman",
    2 : 12
}

my_dict = {"name":"Azman" , "age": 12}
print(my_dict["name"])
print(my_dict.get("age"))

my_dict["age"] = 13
print(my_dict)

my_dict["city"] = "Dhaka"
print(my_dict)

my_dict.pop("age")
print("Updated Dictionary:", my_dict)

my_dict.clear()
print("Cleared Dictionary:", my_dict)