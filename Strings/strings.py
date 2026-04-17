# Method 1
def reversingNaieve(text):
    rev = ''
    for i in range(len(text)-1, -1, -1):
        rev += text[i]
    return rev

text_input = input("Enter Your Text You Want To Reverse: ")
print(f"The Bruteforce Approach To Reversing A String, {text_input} : {reversingNaieve(text_input)}")
print(f"Time Complexity: O(n), Space Complexity: O(n)")

# Method 2
def reversingBetter(text):
    rev = ''
    size = len(text)
    text = list(text)
    for i in range(size // 2):
        text[i], text[size - i - 1] = text[size - i - 1], text[i]
    return "".join(text)

text_input = input("Enter Your Text You Want To Reverse: ")
print(f"The Better Bruteforce Approach To Reversing A String, {text_input} : {reversingNaieve(text_input)}")
print(f"Time Complexity: O(n/2), Space Complexity: O(n)")

# Method 3
print(f"The Best Approach To Reverse A String, {text_input} : {text_input[:: -1]}")
print(f"Time Complexity: O(1), Space Complexity: O(1)")