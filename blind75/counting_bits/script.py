def counting_bits (a : int) -> list[int]:
    result = []
    for n in range(a+1):
        sum = 0
        while n != 0:
            sum += n % 2
            n = n >> 1
        result.append(sum)
    return result

print(counting_bits(0))