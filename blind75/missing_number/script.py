def missing_number(arr: list[int]) -> int:
    n = len(arr)
    sum = 0
    for i in range(1,n+1):
        # sum += i
        # sum -= arr[i-1]
        sum += i - arr[i-1]
    return sum

# print(missing_number([3,0,1]))