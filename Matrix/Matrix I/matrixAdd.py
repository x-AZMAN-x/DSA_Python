<<<<<<< HEAD
#Initializing Matrices
x = [[8, 2], 
    [4, 1]]
y = [[3, 8], 
    [9, 15]]

ans = [[0, 0], [0, 0]]

for i in range(len(x)): #Rows
    for j in range(len(x[0])): #Individual Columns
        ans[i][j] = x[i][j] + y[i][j]

=======
#Initializing Matrices
x = [[8, 2], 
    [4, 1]]
y = [[3, 8], 
    [9, 15]]

ans = [[0, 0], [0, 0]]

for i in range(len(x)): #Rows
    for j in range(len(x[0])): #Individual Columns
        ans[i][j] = x[i][j] + y[i][j]

>>>>>>> b1f64800806b5efb3ee933d6fee0f2277400a99e
print(ans)