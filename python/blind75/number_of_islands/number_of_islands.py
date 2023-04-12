# from collections import deque 

# def numIslands(grid: 'list[list[str]]') -> int:
#     if grid == []: return 0
    
#     rows = len(grid)
#     columns = len(grid[0])
#     islands = 0

#     rootsList = [i for i in range(rows * columns)]
#     visited = set()

#     def bfs(r : int, c : int):
#         q = deque()
#         visited.add((r,c))
#         q.append((r,c))
#         while q:
#             r, c = q.popleft()
#             directions = [[1,0],[-1,0],[0,1],[0,-1]]
#             for dr, dc in directions:
#                 if ((r + dr) in range(rows) and 
#                 (c + dc) in range (columns) and
#                 grid[r + dr][c + dc] == "1" and
#                 (r + dr, c + dc) not in visited):
#                     q.append((r + dr, c + dc))
#                     visited.add((r + dr, c + dc))
            

#     for r in range(rows):
#         for c in range(columns):
#             if grid[r][c] == "1" and (r,c) not in visited:
#                 # mark all island grids as visited
#                 bfs(r,c)
#                 islands += 1
#     return islands


def numIslands(grid: 'list[list[str]]') -> int:
    rows = len(grid)
    columns = len(grid[0])
    # ids will be attributed to every item from 0 to rows*columns - 1 in ascending order.
    # example: rows = 3, columns = 2
    # ids: 0 1
    #      2 3
    #      4 5
    rootsList = [i for i in range(rows * columns)]
    def isRoot(nodeId : int, rootsList : 'list[int]') -> bool:
        return rootsList[nodeId] == nodeId
    def connect(nodeId : int, connectToId : int, rootsList : 'list[int]'):
        # node's root is now the same as connectTo's root.
        rootsList[nodeId] = rootsList[connectToId]
    def connected(nodeId : int, node2Id : int, rootList : 'list[int]') -> bool:
        return rootList[nodeId] == rootList[node2Id]
        
    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == "0": continue
            id = r * columns + c
            # down check
            if r != rows - 1 and grid[r + 1][c] == "1":
                connect(rootsList[id + columns], rootsList[id], rootsList)
            # right check
            if c != columns - 1 and grid[r][c + 1] == "1":
                connect(rootsList[id + 1], rootsList[id], rootsList)

    # return rootsList
    # roots = []
    # for r in range(rows):
    #     for c in range(columns):
    #         if grid[r][c] == "0": continue
    #         if isRoot(r * columns + c, rootsList): roots.append((r,c))
    # return roots

    numberOfIslands = 0
    for r in range(rows):
        for c in range(columns):
            if isRoot(r * columns + c, rootsList) and grid[r][c] == "1": numberOfIslands += 1
    return numberOfIslands

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

print(numIslands([
    ["1","0","1","1","0","0","1","0","1","1","1","1","0","1","0","1","1","1","1","0"],
    ["0","1","0","0","1","0","1","0","1","1","1","1","1","1","0","1","1","0","1","1"],
    ["1","0","0","1","0","1","0","1","0","1","1","0","1","1","1","0","0","1","1","0"],
    ["0","1","1","0","0","1","1","0","1","1","1","1","0","0","1","0","0","0","1","1"],
    ["1","1","0","1","0","0","1","0","0","0","1","0","1","0","1","1","1","0","1","1"],
    ["0","0","0","0","1","0","1","1","0","0","1","0","0","1","0","1","1","1","1","0"],
    ["1","0","1","1","1","1","0","1","1","0","1","1","0","1","1","1","0","0","1","0"],
    ["0","1","1","0","0","0","1","0","0","1","0","1","1","1","0","0","1","1","0","1"],
    ["0","0","0","0","1","1","0","1","0","0","1","1","0","1","0","0","1","0","1","0"],
    ["0","0","1","1","1","0","1","0","1","0","1","1","1","0","1","1","1","1","1","0"],
    ["1","0","1","0","1","1","1","0","1","1","1","0","1","0","1","0","1","0","1","1"],
    ["0","0","1","1","1","1","0","1","1","1","0","1","0","0","0","1","1","1","0","1"],
    ["1","1","1","0","0","0","0","0","1","1","0","1","1","1","0","1","1","1","1","0"],
    ["0","0","1","1","1","0","0","1","0","0","1","1","1","1","1","1","0","1","1","0"],
    ["0","0","0","1","1","0","0","0","0","1","1","0","1","0","0","1","1","1","1","1"],
    ["0","1","1","1","0","1","0","0","1","1","1","1","1","0","1","1","1","0","0","1"],
    ["0","0","0","0","1","1","1","1","0","0","0","0","1","0","0","0","0","1","1","0"],
    ["1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1","1","1"],
    ["0","1","0","0","1","0","0","1","1","1","1","1","1","0","1","0","1","1","1","1"],
    ["0","0","1","1","1","1","1","0","0","0","1","1","1","1","1","1","0","1","1","0"]]))