def numberConnected (n : 'int', edges : 'list[list[int]]') -> 'int':
    roots = [i for i in range(n)]

    for one, two in edges:
        if roots[one] != roots[two]:
            roots[two] = roots[one]
    
    count = 0
    for node in range(n):
        if roots[node] == node: count += 1
    
    return count
    
print(numberConnected(5, [[0,1],[1,2],[3,4]]))