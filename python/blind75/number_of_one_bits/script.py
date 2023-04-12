# def no_of_one_bits (n : int) -> int:
#     result = 0
#     while n:
#         result += n % 2
#         n = n >> 1
#     return result

# alternatively

def no_of_one_bits (n : int) -> int:
    result = 0
    while n:
        n = n & (n-1)
        result += 1
    return result