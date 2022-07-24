def computeLongestIncreasingSubsequence(arr : "list[int]")->"list[int]":
    
    for i in range(len(arr)).reverse(): # every number
        for j in range(len(arr)): # every number
            pass

# print(computeLongestIncreasingSubsequence([1,2,3,4,5,6,7]))
# print(computeLongestIncreasingSubsequence([0,1,2,5,6,7]))
# print(computeLongestIncreasingSubsequence([2,2,2,2,2,2,1]))
# print(computeLongestIncreasingSubsequence([0,2,1,3,1,4,1,5]))