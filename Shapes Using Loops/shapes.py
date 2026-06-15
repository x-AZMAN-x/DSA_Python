shape = input("Which Shape Do You Want To Create (1. Right-Angled Triangle, 2. Right Angle, 3. Pyramid, 4. Reversed Pyramid, 5. Side Triangle, 6. Reversed Right Angle, 7. A, 8. B, 9. C, 10. D): ")

if shape == "Right Angled Triangle" or shape == "Right-Angled Triangle" or shape == "Right angled triangle" or shape == "right angled triangle" or shape == "right-angled triangle" or shape == "1":
    rows = int(input("Enter The Number Of Rows: "))

    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end = " ")
        print()
    
elif shape == "Right Angle" or shape == "Right angle" or shape == "right angle" or shape == "2":
    rows = int(input("Enter the Number Of Rows: "))

    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end = " ")
        print()

elif shape == "Pyramid" or shape == "pyramid" or shape == "3":
    rows = int(input("Enter the Number Of Rows: "))

    for i in range(0, rows):
        for j in range(0, rows - i - 1):
            print(end=" ")
        for j in range(0, i + 1):
            print("*", end = " ")
        print()

elif shape == "Reversed Pyramid" or shape == "Reversed pyramid" or shape == "reversed pyramid" or shape == "4":
    rows = int(input("Enter the Number Of Rows: "))

    for i in range(rows, 0, -1):
        for j in range(0, rows - i):
            print(end= " ")
        for j in range(0, i):
            print("*", end = " ")
        print()

elif shape == "Side Triangle" or shape == "Side triangle" or shape == "side triangle" or shape == "5":
    rows = int(input("Enter the Number Of Rows: "))

    for i in range(rows):
        print(''*(rows-i-1)+'* '*(i+1))
    for j in range(rows-1,0,-1):
        print(''*(rows-j)+'* '*(j))

elif shape == "Reversed Right Angle" or shape == "Reversed right angle" or shape == "reversed right angle" or shape == "Reversed Right angle" or shape == "6":
    rows = int(input("Enter the Number Of Rows: "))

    for i in range(rows, 0, -1):
        for j in range(0, i):
            print("*", end = " ")
        print()

elif shape == "A" or shape == "a" or shape == "7":

    for row in range(7):
        for col in range(5):
            if (col == 0 or col == 4) or ((row == 0 or row == 3) and (col > 0 and col < 4)):
                print("*", end = "")
            else:
                print(end = " ")
        print()

elif shape == "B" or shape == "b" or shape == "8":
    
    for row in range(7):
        for col in range(5):
            if (col == 0) or (col == 4 and (row != 0 and row != 6)) or ((row == 0 or row == 3 or row == 6)) and (col > 0 and col < 4):
                print("*", end= "")
            else:
                print(end= " ")
        print()

elif shape == "C" or shape == "c" or shape == "9":
    
    for row in range(7):
        for col in range(5):
            if (col == 0) or ((row == 0 or row == 6) and (col > 0)):
                print("*", end= "")
            else:
                print(end= " ")
        print()

elif shape == "D" or shape == "d" or shape == "10":

    for row in range(7):
            for col in range(5):
                if (col == 0) or (col == 4 and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col > 0 and col < 4)):
                    print("*", end= "")
                else:
                    print(end= " ")
            print()

else:
    print("Invalid Option! Please Choose A Valid One.")