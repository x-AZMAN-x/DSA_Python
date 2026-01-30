def cntSubarrays(arr, k):
  
    # Dictionary To Store Prefix Sums Frequencies
    prefixSums = {}
    res = 0
    currSum = 0

    for val in arr:
        # Add Current Element To Sum So Far
        currSum += val

        # If currSum Is Equal To Desired Sum
        # Then A New Subarray Is Found
        if currSum == k:
            res += 1

        # Check If The Difference Exists
        # In The prefixSums Dictionary
        if currSum - k in prefixSums:
            res += prefixSums[currSum - k]

        # Add currSum To The Dictionary Of Prefix Sums
        prefixSums[currSum] = prefixSums.get(currSum, 0) + 1

    return res

if __name__ == "__main__":
    arr = [10, 2, -2, -20, 10]
    k = -10
    print(cntSubarrays(arr, k))