def substring(t1, t2):
    if t1 == t2:
        return True
    if len(t1) == 0 or len(t2) == 0:
        return False
    
    return t2 in t1

text1 = input("Enter The First Text: ")
text2 = input("Enter The Second Text: ")
print(substring(text1, text2))