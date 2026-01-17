def trappedWater(h):
    if not h or len(h) < 3:
        return 0
    
    n = len(h)
    left = 0
    right = n - 1
    maxLeft = 0
    maxRight = 0
    total_water = 0

    while left <= right:
        if h[left] <= h[right]:
            if h[left] >= maxLeft:
                maxLeft = h[left]
            else:
                total_water += maxLeft - h[left]
                left += 1
        else:
            if h[right] >= maxRight:
                maxRight = h[right]
            else:
                total_water += maxRight - h[right]
            right -= 1
    return total_water

print(trappedWater([3, 0 , 1, 0, 2, 0, 4]))