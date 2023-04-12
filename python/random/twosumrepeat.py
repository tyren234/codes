def twosum(arr : "list[int]", target : int) -> tuple:
    wanted = dict()
    for i in range(len(arr)):
        if wanted.get(target-arr[i]) != None:
            return (wanted.get(target-arr[i]), i)
        
        wanted[arr[i]] = i

print(twosum([1,2,3,4,5,6,1,7,8],2))
        