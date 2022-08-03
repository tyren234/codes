def decodeWays (digits : str) -> int:
    def checkForTwoDigitNumber (first: chr, second: chr) -> bool:
                if (first == '1' and '1' <= second <= '9'): return True
                if (first == '2' and '1' <= second <= '6') : return True
                return False

    if digits == [0]: return 0

    outcomes = [1] * (len(digits)+1)

    for i in reversed(range(len(digits))):
        # if the number is 0 and the previus number isn't either 1 or 2 then stop an return 0. We can't make any number with 0 other than 10 and 20.
        if digits[i] == "0":
            # if either this is the first element (so there is no previous one) or the number behind 0 is neither 1 nor 2.
            if i <= 0 or (digits[i-1] != '1' and digits[i-1] != '2'):
                return 0
            outcomes[i] = outcomes[i+1]
            digits = digits[:i-1] + 'x' + digits[i:]
        else:
            outcomes[i] = outcomes[i+1]
            if i != len(digits)-1 and checkForTwoDigitNumber(digits[i],digits[i+1]):
                outcomes[i] += outcomes[i+2]
        # print(i, outcomes, digits)
    return outcomes[0]


# print(decodeWays("12"))
# print(decodeWays("226"))
# print(decodeWays("06"))
# print(decodeWays("2101"))
print(decodeWays("1201234")) # 3

# digits = "witam"
# digits = digits[:2-1] + 'x' + digits[2:]
# print(digits)
