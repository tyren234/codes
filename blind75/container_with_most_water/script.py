def container_with_most_water(arr : list[int]) -> int:
    l = 0
    r = len (arr) - 1
    cmax = (r-l) * min(arr[l], arr[r])
    while l < r:
        if arr[l] < arr[r]:
            l += 1
        else:
            r -= 1
        # alternatively these ifs can be added, but this doesn't make a difference
        # elif arr[l] > arr[r]:
        #     r -= 1
        # else: # if next left is larget then next right shift left
        #     if arr[l+1] > arr[r-1]:
        #         l += 1
        #     else: # else shift right
        #         r -= 1
        cmax = max(cmax, (r-l)*min(arr[l],arr[r]))
    
    return cmax
        