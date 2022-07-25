from numpy import size


def longest_common_subsequence(text1 : str, text2 : str) -> str:
    sizes = dict()
    for i in reversed(range(len(text2))):
        for j in range(len(text1)):
            if text1[j] == text2[i]:
                cmax = 1
                for k in range(j+1, len(text1)):
                    if sizes.get(text1[k]) != None and sizes.get(text1[k]) + 1 > cmax:
                        cmax = 1 + sizes[text1[k]]
                if sizes.get(text2[i]) == None or sizes.get(text2[i]) < cmax:
                    sizes[text2[i]] = cmax
    if not sizes: return 0
    return max(sizes.values())
        

# print(longest_common_subsequence("bcade", "acekf")) # 2
print(longest_common_subsequence("abcba", "abcbcba")) # 5
    