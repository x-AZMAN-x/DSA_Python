def find_duplicate(text):
    seen = set()
    for char in text:
        if char in seen:
            return char
        seen.add(char)
    return None

text = input("Enter Your Text: ")
print(find_duplicate(text))