# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/
def two_sum_II (arr : list[int], target : int) -> tuple:
    l = 0
    r = len(arr) - 1
    while l <= r:
        if arr[l] + arr[r] == target: return (l+1, r+1)
        elif arr[l] + arr[r] > target: r -= 1
        else: l += 1
    return -1

# print(two_sum_II([1,3,4,5,7,11],9))
