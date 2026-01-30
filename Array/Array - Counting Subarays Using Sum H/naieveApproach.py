def cntSubarrays(arr, k):
    
    # For Maintaining The Count Of 
    # Subarrays Whose Sum Equal To K
    count = 0
    n = len(arr)

    for i in range(n):
        currSum = 0

        # Subarray From i To Each j = Arr[i....j]
        for j in range(i, n):
            currSum += arr[j]

            # Increment Count If The currSum Equals K
            if currSum == k:
                count += 1
                
    return count


if __name__ == "__main__":
    arr = [10, 2, -2, -20, 10]
    k = -10
    print(cntSubarrays(arr, k))