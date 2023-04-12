from distutils.log import error


def maximum_subarray(arr : list[int]) -> int:
    if len(arr) == 0: return -1
    sum = 0
    cmax = arr[0]
    for i in range(len(arr)):
        sum += arr[i]
        if sum > cmax:
            cmax = sum
        if sum < 0:
            sum = 0
    return cmax
            
# print(maximum_subarray([-2,1,-3,4,-1,2,1,-5,4]))