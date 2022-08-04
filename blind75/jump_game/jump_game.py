# O(n^2) solution - too slow
# def canJump(nums:"list[int]") -> bool:
#     outcome = [False] * len(nums)
#     outcome[-1] = True
#     for i in reversed(range(len(nums)-1)):
#         for k in range(1,nums[i]+1):
#             if k+i < len(nums) and outcome[k+i]: # == True
#                 outcome[i] = True
#                 break
#     return outcome[0]

# O(n) solution - linear time, best option
def canJump(nums:"list[int]") -> bool:
    target = len(nums) - 1
    for i in reversed(range(len(nums)-1)):
        if i + nums[i] >= target: target = i
    return True if not target else False

# print(canJump([2,3,1,1,4]))
# print(canJump([3,2,1,0,4]))