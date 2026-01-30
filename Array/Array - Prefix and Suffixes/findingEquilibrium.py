def findingEquilibrium(arr):
    size = len(arr)
    prefix = [0] * size
    suffix = [0] * size

    #Initialize The Ends Of Prefix And Suffix Arrays
    prefix[0] = arr[0]
    prefix[size - 1] = arr[size - 1]

    #Calculate Prefix Sum For All Indices
    for i in range(1, size):
        prefix[i] = prefix[i - 1] + arr[i]
    
    #Calculate Suffix Sum For All Indices
    for i in range(size - 2, -1, -1):
        suffix[i] = suffix[i + 1] + arr[i]

    #Checking If Prefix Sum Is Equals To Suffix Sum
    for i in range(size):
        if prefix[i] == suffix[i]:
            return i
        
    #If Equilibrium Index Doesn't Exist
    return -1

array = [-7, 1, 5, 2, -4, 3, 0]
print(findingEquilibrium(array))