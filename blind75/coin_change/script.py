from sympy import true


def coinChange(coins: list[int], amount: int) -> int:
    coins.sort(reverse=True)
    count = 0
    i = 0
    while amount > 0 and i < len(coins):
        count += amount // coins[i]
        amount = amount % coins[i]
        i += 1
    if amount != 0:
        return -1
    return count

print(coinChange([3,2,1], 15))
