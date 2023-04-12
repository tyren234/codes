def rob(nums : "list[int]") -> int:
    if len(nums) == 1: return nums[0]
    def rob1 (nums1 : "list[int]") -> int:
        prev, neighbor = 0,0
        for number in nums1:
            temp = max(number + prev, neighbor)
            prev = neighbor
            neighbor = temp
        return neighbor

    return max(rob1(nums[1:]),rob1(nums[:-1]))

# print(rob([2,3,2]))
# print(rob([1,2,3,1]))
# print(rob([1,2,3]))