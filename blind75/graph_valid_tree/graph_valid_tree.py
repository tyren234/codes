def isTree (n : int, edges : 'list[list[int]]') -> bool:
    if n <= 2: return True
    connections = dict([(i, set()) for i in range(n)]) # creates a dictionary with keys range(n) and [] in each key
    for pair in edges:
        connections[pair[0]].add(pair[1])
        connections[pair[1]].add(pair[0])

    visited = set()
    
    def dfs(node : 'int', previous : 'int'):
        if node in visited: return False
        visited.add(node)
        for child in connections[node]:
            if child != previous: dfs(child, node)

    if dfs(0,-1) == False: return False

    return len(visited) == n


print(isTree(5, [[0,1],[0,2],[0,3],[1,4]]))