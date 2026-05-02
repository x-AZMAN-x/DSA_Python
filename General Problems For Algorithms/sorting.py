# First Approach
text = input("Enter Your Text To Sort: ")
sort = sorted(text)
sorted_text = "".join(sort)
print(sorted_text)

# Quick Sort Approach
def quickSort(text):
    if len(text) <= 1:
        return text
    pivot = text[0]
    less = [x for x in text[1:] if x <= pivot]
    greater = [x for x in text[1:] if x > pivot]
    return quickSort(less) + [pivot] + quickSort(greater)

print("".join(quickSort(text)))