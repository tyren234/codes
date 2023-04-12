# just checking if I can still solve the coin change problem.
import math

def coinChange(coins: "list[int]", amount: int) -> int:
    sizes = [0]
    for i in range(1, amount+1):
        cmin = math.inf
        for coin in coins:
            if i < coin: continue
            if cmin > 1 + sizes[i-coin]:
                cmin = 1 + sizes[i-coin]
        sizes.append(cmin)
    if sizes[-1] == math.inf: return -1
    return sizes[-1]

# print(coinChange([1], 0))

# And I'm praud to say - I still can :)
# (Although it took me a while - I did it)