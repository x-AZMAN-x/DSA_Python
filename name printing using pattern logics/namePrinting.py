for row in range(7):
        for col in range(5):
            if (col == 0 or col == 4) or ((row == 0 or row == 3) and (col > 0 and col < 4)):
                print("*", end = "")
            else:
                print(end = " ")
        print()

i = 1
j = 4

for row in range(0,6):
    for col in range(0,6):
        if row == 0 or row == 5:
            print("*", end = "")
        elif row == i and col == j:
            print("*", end = "")
            i = i + 1
            j = j - 1
        else:
            print(end = " ")
    print()   

for row in range(7):
    for col in range(7):
        if (col == 0 or col == 6) or (row == col and (col > 0 and col < 4)) or (row == 1 and col == 5) or (row == 2 and col == 4):
            print("*", end="")
        else:
            print(" ", end="")
    print()

for row in range(7):
        for col in range(7):
            if (col == 0 or col == 4) or ((row == 0 or row == 3) and (col > 0 and col < 4)):
                print("*", end = "")
            else:
                print(end = " ")
        print()

for row in range(0, 6):
    for col in range(0, 6):
        if (col == 0 or col == 5 or row == col):
            print("*", end="")
        else:
            print(" ", end="")
    print()