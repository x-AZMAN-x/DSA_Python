queue = []   # Blank Queue

print(queue)   # Displaying A Blank Queue

# Adding Elements To The Queue/ Enqueue
queue.append("Player1")
queue.append("Player2")
queue.append("Player3")

print(queue)   # Displaying The Queue

# Removing Elements From The Queue/ Dequeue
queue.pop(0)
print(queue)   # To Make Sure If The Elements Are Getting Removed Who Enqued First
queue.pop(0)
queue.pop(0)

print(queue)

# Not Recommended Because If There Are A Lot Of Elements, Then There Would Be Problems For Popping In The List