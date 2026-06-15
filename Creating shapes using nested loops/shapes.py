n_rows = int(input("Enter The Rows: "))
n_cols = int(input("Enter The Columns: "))
shape = input("Which Shape Do You Want To Create (1. Checkerboard, 2. Diamond) Type The Name Or Number Of The Shape: ")

if shape == "Checkerboard" or shape == "1" or shape == "checkerboard":
    for rows in range(n_rows):
        for cols in range(n_cols):
            if (rows + cols)%2 == 0:
                print(0, end= " ")
            else:
                print(1, end=" ")
        print()

elif shape == "Diamond" or shape == "diamond" or shape == "2":
    def diamond(rows):
        for i in range(rows):
            print('' * (rows- i - 1) + '1' * (i + 1))
        for j in range(rows - 1, 0, -1):
            print('' * (rows - j) + '1' * (j))

    diamond(n_rows)

else:
    print("Not A Valid Option! Please Choose A Valid One.")