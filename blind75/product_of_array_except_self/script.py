from audioop import mul


nums = [-1,1,0,-3,3]
out = [1]*len(nums)
out2 = [1]*len(nums)

multiplyer = 1
#all previous 
for i in range(1,len(nums)):
    multiplyer = nums[i-1] * multiplyer
    out[i] = multiplyer

multiplyer = 1
#all following
for i in reversed(range(0,len(nums)-1)):
    multiplyer = nums[i+1] * multiplyer
    out[i] *= multiplyer

print(out)
 