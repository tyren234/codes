from collections import deque 

def numIslands(grid: 'list[list[str]]') -> int:
    if grid == []: return 0
    
    rows = len(grid)
    columns = len(grid[0])
    islands = 0

    rootsList = [i for i in range(rows * columns)]
    visited = set()

    def bfs(r : int, c : int):
        q = deque()
        visited.add((r,c))
        q.append((r,c))
        while q:
            row, col = q.popleft()
            

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == "1" and (r,c) not in visited:
                # mark all island grids as visited
                bfs(r,c)
                islands += 1
    return islands



# print(numIslands([
# ["1","1","1","1","0"],
# ["1","1","0","1","0"],
# ["1","1","0","0","0"],
# ["0","0","0","0","0"]]))

# print(numIslands([
#     ["1","1","1"],
#     ["0","1","0"],
#     ["1","1","1"]]))

# print(numIslands([
#     ["1","0","1","1","1"],
#     ["1","0","1","0","1"],
#     ["1","1","1","0","1"]]))

# # (0,6)(4,2)(4,7)
# print(numIslands([
#     ["1","1","1","1","1","0","1","1","1","1"],
#     ["1","0","1","0","1","1","1","1","1","1"],
#     ["0","1","1","1","0","1","1","1","1","1"],
#     ["1","1","0","1","1","0","0","0","0","1"],
#     ["1","0","1","0","1","0","0","1","0","1"],
#     ["1","0","0","1","1","1","0","1","0","0"],
#     ["0","0","1","0","0","1","1","1","1","0"],
#     ["1","0","1","1","1","0","0","1","1","1"],
#     ["1","1","1","1","1","1","1","1","0","1"],
#     ["1","0","1","1","1","1","1","1","1","0"]]))