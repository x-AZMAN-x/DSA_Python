text = "Hello Python World!"
print(text)
print(len(text))

print(text[0:5])
print(text[7:13])
print(text[7:])
print(text[:5])
print(text[:])

print(text[-6:])
print(text[-11:-6])
print(text[:-7])

print(text[::2])
print(text[::-1])
print(text[7:13:2])

greeting = "Hello"
name = "Azman"
print(greeting + ", "+ name + "!")

message = "Hello"
message += ", Python!"
print(message)
words = ["Hello", "Python", "World"]
joined = " ".join(words)
print(joined)

csv = ", ".join(["apple", "banana", "cherry"])
print(csv)

new_text = text.replace("Python", "JavaScript")
print(new_text)

print(text[6:])

print(text[:-7])

print(text[:5] + " " + text[13:])