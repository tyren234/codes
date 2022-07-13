def min_in_rotated_sorted_array (arr : list[int]) -> int:
    if len(arr) == 0: return None
    m = len(arr)//2
    if arr[m] >= arr[0]:
        # look right
        while True:
            if m >= len(arr)-1: return arr[0]
            elif arr[m] > arr[m+1]: return arr[m+1]
            else: m += 1
    else:
        # look left
        while True:
            if m <= 0: return arr[0]
            elif arr[m] < arr[m-1]: return arr[m-1]
            else: m -= 1

# print(min_in_rotated_sorted_array([2,5,8,11,13,57,9458,10000]))