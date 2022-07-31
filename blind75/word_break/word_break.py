def wordBreak(s : str, wordDict : "list[str]") -> bool:
    outcomes = [False] * (len(s) + 1)
    outcomes[len(s)] = True

    for i in reversed(range(len(s))):
        for word in wordDict:
            if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                outcomes[i] = outcomes[i+len(word)]
            if outcomes[i] == True: # if we found matching word already, just break
                break
    return outcomes[0]