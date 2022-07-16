def min_in_rotated_sorted_array (arr : list[int]) -> int:
    # res = arr[0]
    # l = 0
    # r = len(arr) - 1

    # while l<=r:
    #     if arr[l] < arr[r]:
    #         res = min(res, arr[l])
    #         break
        
    #     m = (l+r)//2
    #     res = min(res,arr[m])
    #     if arr[m] >= arr[l]:
    #         l = m + 1
    #     else: 
    #         r = m - 1
        
    # return res

    l = 0
    r = len(arr) - 1
    res = arr[0]

    while l <= r:
        if arr[l] <= arr[r]:
            res = min(res, arr[l])
            break
        
        m = (l+r)//2
        res = min(res, arr[m])
        if arr[m] < arr[l]:
            r = m - 1
        else:
            l = m + 1
    return res

# 0,1,2,3,4,5,6,7
# 7,0,1,2,3,4,5,6
# 6,7,0,1,2,3,4,5
# 5,6,7,0,1,2,3,4
# 4,5,6,7,0,1,2,3
# 3,4,5,6,7,0,1,2
# 2,3,4,5,6,7,0,1
# 1,2,3,4,5,6,7,0
# 0,1,2,3,4,5,6,7

# print(min_in_rotated_sorted_array([11,13,57,9458,10000,2,5,8]))