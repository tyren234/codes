def maximum_product_subarray(arr : list[int]) -> int:
    if len(arr) == 0:return 0
    cmax = 1
    cmin = 1
    current = max(arr)
    for i in range(len(arr)):
        tmp = arr[i] * cmax
        cmax = max(cmax * arr[i], cmin * arr[i], arr[i])
        cmin = min(tmp, cmin * arr[i], arr[i])
        current = max(current, cmax)

    return current

#print(maximum_product_subarray([2,3,-2,4]))
#print(maximum_product_subarray([-1,-2,-3]))
#print(maximum_product_subarray([-1,-2,-3,-4, 0, 15, 3]))

