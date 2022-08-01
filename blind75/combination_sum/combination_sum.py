def combinationSum (candidates : "list[int]", target : int) -> "list[list[int]]":
    res = []

    # deph first search
    def dfs(i : int, cur : "list[int]", total : int): 
        """
        Arguments:
            i - index of current candidate in candidates list
                cur - current answer (a list of integers such as [2,2,3,6])
                    total - sum of cur
        """
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return

        # we decide to include this candidate
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        cur.pop() # remember to pop previously added value

        # we decide not to include this candidate and go to the next one
        dfs(i+1, cur, total)
    
    dfs(0,[],0)

    return res

# print(combinationSum([2,3,6,7],7))
# print(combinationSum([2,3,5],8))

