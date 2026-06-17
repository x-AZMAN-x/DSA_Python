import sys          # To handle Errors
def generateShape(n, shape):
    """
    Arguments:
        n Is The Grid Size
        shape Can Be Either A Checkerboard Or A Diamond
    Returns A 2D Shape Of Integers Representing The Pattern, 0 Showing The Background And 1 Showing The Shape.
    """

    # For each row, create a list of columns
    # (i + j)%2 gives alternating 0 and 1, where it returns 0 when (i + j) is even and returns 1 when (i + j) is odd
    if shape == "Checkerboard" or shape == "1" or shape == "checkerboard":
        for rows in range(n):
            for cols in range(n):
                if (rows + cols)%2 == 0:
                    print(0, end= " ")
                else:
                    print(1, end=" ")
            print()

    # For a diamond shape, n is guranteed odd
    elif shape == "Diamond" or shape == "diamond" or shape == "2":
        def diamond(rows):
            for i in range(rows):
                print('' * (rows- i - 1) + '1' * (i + 1))
            for j in range(rows - 1, 0, -1):
                print('' * (rows - j) + '1' * (j))

        diamond(n)
    # If the user's answer is not a valid option, show an error
    else:
        print("Not A Valid Option! Please Choose A Valid One.")

# Main execution block
if __name__ == "__main__":
    # Runs only when the script is executed directly
    try:
        # Row, strip whitespace, convert to integer
        row = int(input().strip())
        # Shape, strip whitespace, keep as string
        shape = input().strip()
        # Calling the function
        res = generateShape(row, shape)
        for i in res:
            print(" ".join(str(x) for x in i))
        
    except ValueError as e:
        # Error when conversation to int fails
        print(f"Input Error: {e}", file = sys.stderr)
        sys.exit(1)          # Exit with error code 1
    
    except EOFError:
        # If input is missing, print error and exit with error code 1
        print("Error: Not Enough Input Lines Provided.", file = sys.stderr)
        sys.exit(1)
    
    except Exception as e:
        # Error if there is any other unexpected exceptions
        print(f"An Unexpected Error Occured: {e}", file = sys.stderr)
        sys.exit(1)