#Initializing Matrices
x = [[8, 2], 
    [4, 1]]
y = [[3, 8], 
    [9, 15]]

ans = [[0, 0], [0, 0]]

#Size Of The Result Matrix(multi) => Rows In First Matrix == Columns In Second Matrix

for i in range(len(x)): #Rows Of The First Matrix x
    for j in range (len(y[0])): # Columns Of The Second Matrix
        for k in range(len(y)): #Rows Of The Second Matrix
            ans[i][j] += x[i][k] * y[k][j]
        
print(ans)