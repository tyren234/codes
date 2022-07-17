def three_sum(arr : list[int]) -> list[list[int]]:
    if len(arr) < 3:
        return -1

    arr.sort()
    solution = []

    for i in range(len(arr)-2):
        if i > 0 and arr[i] == arr[i-1]: # if item is the same as the previous one, continue
            # print("continuing on", i)
            continue

        target = -arr[i]
        l = i + 1
        r = len(arr) - 1
        while l < r:
            if arr[l] + arr[r] == target: 
                if r < len(arr) - 1 and arr[r] != arr[r+1] or r == len(arr) - 1:
                    # print("adding on",i)
                    solution.append([arr[i],arr[l],arr[r]])
                r -= 1
                # l += 1 # might be just as well
            elif arr[l] + arr[r] < target: l += 1
            else: r -= 1

    # for sol in solution:
    #     sol.sort()
    return solution

# print (three_sum([2,4,5,1,5,6,1,9,0,7,5]))
# print (three_sum([-3,3,4,-3,1,2]))
# print (three_sum([-1,0,1,2,-1,4]))
# print (three_sum([-1,0,1,2,-1,-4]))
# print (three_sum([0,0,0,0]))