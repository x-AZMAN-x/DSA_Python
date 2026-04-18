string1 = "Hello Python!"

"""
Generalized Syntax:
variable = my_string.method_name()
"""

#Capitalizing
text = "python is fun"
capitalizedText = text.capitalize()
print(capitalizedText)

#Title Case
print(text.title())

text2 = "PyThOn Is So FuN"
lowercasedText2 = text2.lower()
print(lowercasedText2)

uppercasedText2 = text2.upper()
print(uppercasedText2)

is_lower = text.islower()
print(is_lower)
is_upper = text.isupper()
print(is_upper)

#Swapping Case
print(text2.swapcase)

#Checking Alpha Numerics
text3 = "Hi123"
print(text3.isalnum()) #This Checks If There Is Either Alphabets Or Numbers

numbers = "123456"
print(numbers.isdigit())

#Removing Whitespaces From A String
text4 = "Hello Python"
print(text4.rstrip()) #Right Strip
print(text4.strip()) #Full Strip

#Replacing Character In A String
print(text4.replace("Hello", "Hi"))

#Joining String From An Iterable
"""
Syntax:
separator.join(iterable)

Iterable = Array(Lists, Tuples) And Strings
"""

stringList = ["Early", "To", "Bed", "Early", "To", "Rise"]
print(" ".join(stringList))
print("==>".join(stringList))

#Counting The Substrings
my_string = "Python Is Pythonic And I Love Coding In Python"
print(my_string.count("Python"))
print(my_string.count("I"))

#Finding Out The Ascii/Unicodes Of A Character
my_text = input("Enter A Character")
print(ord(my_text)) #Every Character Gets Converted Into Integers
print(bin(ord(my_text))) #Converting A Character Into Machine Readable Binary