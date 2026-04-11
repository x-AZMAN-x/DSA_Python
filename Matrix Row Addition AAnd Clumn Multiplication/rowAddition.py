# Answer Is Not Correct, But I Tried
A = [[1, 2], 
    [3, 4]]

result = [[0, 0], [0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result = [len(A[0]) + len(A[1])], [len(A[1]) + len(A[1])]

print(result)