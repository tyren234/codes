def computeLongestIncreasingSubsequence(arr : "list[int]")->"list[int]":
    
    for i in range(len(arr)).reverse(): # every number
        for j in range(len(arr)): # every number
