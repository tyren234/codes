def search_in_rotated_sorted_array(arr : list[int], x : int) -> int:
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = (l+r)//2
        if arr[m] == x:
            return m

        if arr[m] < arr[l]:
            # m is in the "smaller" part, that means the numbers to the right from m are only larger
            # e,f,a, m, b,c,d
            if x < arr[m] or x > arr[r]:
                # x is to the left of arr[m]
                r = m - 1
            else: #(x > arr[m] and x < arr[l])
                # and x is to the right of arr[m]
                l = m + 1
        else:
            # m is in the "bigger" part, that means the numbers to the left are only getting smaller
            if x > arr[m] or x < arr[l]:
                # x is to the right of arr[m]
                l = m + 1
            else:
                # x is to the left of arr[m]
                r = m - 1
    return -1

# 0,1,2,3,4,5,6,7
# 7,0,1,2,3,4,5,6
# 6,7,0,1,2,3,4,5
# 5,6,7,0,1,2,3,4
# 4,5,6,7,0,1,2,3
# 3,4,5,6,7,0,1,2
# 2,3,4,5,6,7,0,1
# 1,2,3,4,5,6,7,0
# 0,1,2,3,4,5,6,7
#print(search_in_rotated_sorted_array([0,1,2,3,4,5,6,7],3))