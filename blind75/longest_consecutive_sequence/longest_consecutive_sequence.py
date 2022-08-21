def longestConsecutive(nums: 'list[int]') -> 'int':
    sizes = dict()
    # O(n)
    for n in nums:
        sizes[n] = 1
    
    def countSize(n : 'int') -> 'int':
        size = 1
        if n - 1 not in sizes:
            sizes[n] = 1
            return 1
        elif sizes[n] > 1: # already visited
            return sizes[n]
        else:
            sizes[n] = countSize(n - 1) + 1
        return sizes[n]

    # O(n)
    cmax = 0
    for n in nums:
        if sizes.get(n) == 1:
            countSize(n)
            if sizes.get(n) > cmax:
                cmax = sizes.get(n)
    
    return cmax

print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))