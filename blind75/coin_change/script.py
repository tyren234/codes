import math
# I honestly can't describe how this works because I would take me too long.
# There is a saying that you only really understand something when you can teach a baby do it...
# According to this saying I don't uderstand it one bit.
def coinChange(coins: list[int], amount: int) -> int:
    results = [0]
    for camount in range (1,amount+1):
        cmin = math.inf
        for coin in coins:
            if coin > camount:  continue
            temp = 1 + results[camount-coin]
            cmin = min(temp,cmin)
        results.append(cmin)
    if results[-1] == math.inf: return -1
    return results[-1]

print(coinChange([1,3,4,5], 7))
