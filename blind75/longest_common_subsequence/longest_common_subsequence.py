from numpy import size


def longest_common_subsequence(text1 : str, text2 : str) -> str:
    sizes = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
    for i in reversed(range(len(text1))):
        for j in reversed(range(len(text2))):
            if text1[i] == text2[j]:
                sizes[i][j] = 1 + sizes[i+1][j+1]
            else:
                sizes[i][j] = max(sizes[i][j+1], sizes[i+1][j])
    return sizes[0][0]
        

# print(longest_common_subsequence("bcade", "acekf")) # 2
print(longest_common_subsequence("abcba", "abcbcba")) # 5
    