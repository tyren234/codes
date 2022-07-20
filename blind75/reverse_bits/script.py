def reverse_bits(number : int) -> int:
    omask = 1
    cmask = 1 << 31
    result = 0
    for i in range(32):
        #print(omask,end=",")
        if omask & number != 0:
            result = result | cmask
        cmask = cmask >> 1
        omask = omask << 1
    return result

# print(reverse_bits(1))
# print(reverse_bits(2147483648))
