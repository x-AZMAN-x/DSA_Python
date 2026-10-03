import math
from collections import Counter

def minRabbits(ans):
    """
    ans[i] is how many other rabbits rabbit i claims shares its own color.
    Returns The Smallest Possible Total Number Of Rabbits.
    """

    total = 0

    # Counter turns [1, 1, 2] into [1:2, 2:1]
    # The Two Rabbits Said 1, One Rabbit Said 2
    
    for k, count in Counter(ans).items():
        # A rabbit saying k belongs to a group of k + 1 (the k others, plus itself)
        group_size = k + 1

        # Count Rabbits Must Be Spread Across Groups Of That Size
        # We Round Up, Because A Half-Full Group Still Exists
        groups_needed = math.ceil(count / group_size)

        # Every Group Must be Complete, So Each Contribute Its Full Size - Even The Seats No One Interviewed In
        total += groups_needed * group_size
    
    return total

# Samples
print(minRabbits([1, 1, 2]))          # Ans = 5
print(minRabbits([10, 10, 10]))          # Ans = 11
print(minRabbits([1, 1, 1, 1, 1]))          # Ans = 6 (3 Groups Of 2)
print(minRabbits([0, 0, 1, 1, 1]))          # Ans = 6 (2 Solo + 2 Groups Of 2)

# Wrapper
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    ans = list(map(int, data[1:1 + n]))
    print(minRabbits(ans))