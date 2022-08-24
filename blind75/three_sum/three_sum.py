def threeSum(nums : 'list[int]') -> 'list[list[int]]':
    nums.sort()
    outcomes = list()
    for i in range(len(nums)):
        # if it's the same number - skip, it has already been covered
        if i != 0 and nums[i-1] == nums[i]: continue

        l = i + 1
        r = len(nums) - 1

        while l < r:
            sum = nums[l] + nums[r] + nums[i]
            # if sum > 0 then lower the sum
            if sum > 0: r -= 1
            # if sum < 0 then increase the sum
            if sum < 0: l += 1
            # if sum == 0 then add it to the outcomes
            if sum == 0:
                outcomes.append([nums[i], nums[l], nums[r]])
                r -= 1
                # in case there are a couple of same numers on the right too. Just skip them until you encounter a new one.
                while r > l and nums[r] == nums[r+1]: r -= 1
    return outcomes

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))