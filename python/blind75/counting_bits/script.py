# first method using number of one bits problem - O(n * 32) = O(n)
# def counting_bits (a : int) -> list[int]:
#     result = []
#     for n in range(a+1):
#         sum = 0
#         while n != 0:
#             sum += n % 2
#             n = n >> 1
#         result.append(sum)
#     return result

# second method using maths and very interesting property of binary numbers
# 00000
# 00001
# 00010
# 00011
# 00100
# 00110
# 00101
# 00111

def counting_bits (n : int) -> list[int]:
    bits = [0] * (n+1)
    offset = 1

    for i in range (1, n+1):
        if offset * 2 == i:
            offset = i
        bits[i] = 1 + bits[i-offset]
    return bits

# print(counting_bits(0))