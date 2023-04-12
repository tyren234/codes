def computeLongestIncreasingSubsequence(arr : "list[int]")->int:
    sizes = [0]*len(arr)
    sizes[-1] = 1
    for i in reversed(range(len(arr)-1)): # every number from the penultimate to the first one
        cmax = 1
        for j in reversed(range(i+1,len(arr))): # every number from the last one to the current ith
            if (arr[j] > arr[i] and cmax < 1 + sizes[j]):
                cmax = 1 + sizes[j]
        sizes[i] = cmax
    return max(sizes)
    # return sizes                
# print(computeLongestIncreasingSubsequence([0,1,0,3,2,3]))
# print(computeLongestIncreasingSubsequence([1,3,6,7,9,4,10,5,6]))
# print(computeLongestIncreasingSubsequence([2,2,2,2,2,2,1]))
# print(computeLongestIncreasingSubsequence([0,2,1,3,1,4,1,5]))