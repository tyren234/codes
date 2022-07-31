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

def wordBreak2(s : str, wordDict : "list[str]") -> bool:
    outcomes = [False] * (len(s)+1)
    outcomes[0] = True

    # i - begining of the current word in outcomes
    # i-1 - previous word's result in outcomes - true or false
    # i+len(word)-1 - end of current word in outcomes

    for i in range(1,len(s)+1):
        for word in wordDict:
            if i+len(word)-1 > len(s): continue
            if s[i-1:i-1+len(word)] == word: outcomes[i+len(word)-1] = outcomes[i-1]
            if outcomes[i + len(word) - 1] == True: break
    
    return outcomes[-1]