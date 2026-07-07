import sys # To Handle Errors
def generateShape(n, shape):
   """
   Arguments:
       n Is The Grid Size
       shape Can Be Either A Checkerboard Or A Diamond
   Returns A 2D Shape Of Integers Representing The Pattern, 0 Showing The Background And 1 Showing The Shape.
   """
   result = []
   if shape == "Checkerboard" or shape == "1" or shape == "checkerboard":
       for rows in range(n):
           row_data = []
           for cols in range(n):
               if (rows + cols) % 2 == 0:
                   row_data.append(0)
               else:
                   row_data.append(1)
           result.append(row_data)


   # For a diamond shape, n is guaranteed odd
   elif shape == "Diamond" or shape == "diamond" or shape == "2":
       def diamond(rows):
           grid = []
           c = rows // 2
           for i in range(rows):
               row = []
               for _ in range(rows):
                   row.append(0)
               grid.append(row)


           for i in range(rows):
               for j in range(rows):
                   if abs(i - c) + abs(j - c) <= c:
                       grid[i][j] = 1
           return grid


       result = diamond(n)

    # If the user's answer is not a valid option, show an error
   else:
       raise ValueError("Invalid shape. Use 'checkerboard' or 'diamond'.")


   return result

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
       print(f"Input Error: {e}", file=sys.stderr)
       sys.exit(1)


   except EOFError:
       # If input is missing, print error and exit with error code 1
       print("Error: Not Enough Input Lines Provided.", file=sys.stderr)
       sys.exit(1)


   except Exception as e:
       # Error if there is any other unexpected exceptions
       print(f"An Unexpected Error Occured: {e}", file=sys.stderr)
       sys.exit(1)