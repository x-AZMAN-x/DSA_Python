def removeAllWhitespaces(string):
    """Remove All Whitespace Characters (Spaces, Tabs And New Lines)"""
    return " ".join(string.split())

text = """Hello World
This Is A Test 
    With Tabs And New Lines"""

res = removeAllWhitespaces(text)
print("Original: ", repr(text))
print("Cleaned: ", res)