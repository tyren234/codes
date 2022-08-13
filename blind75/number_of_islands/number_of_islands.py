def numIslands(grid: 'list[list[str]]') -> int:
    rows = len(grid)
    columns = len(grid[0])
    # ids will be attributed to every item from 0 to rows*columns - 1 in ascending order.
    # example: rows = 3, columns = 2
    # ids: 0 1
    #      2 3
    #      4 5

    rootsList = [i for i in range(rows * columns)]

    def isRoot(nodeId : int, rootsList : 'list[int]'):
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
            if r != rows - 1 and grid[r + 1][c] == "1" and not connected(id, id + columns, rootsList):
                if isRoot(id + columns, rootsList): connect(id + columns, id, rootsList)
                else: connect(rootsList[id], id + columns, rootsList)
            # right check
            if c != columns - 1 and grid[r][c + 1] == "1" and not connected(id, id + 1, rootsList):
                if isRoot(id + 1, rootsList): connect(id + 1, id, rootsList)
                else: connect(rootsList[id], id + 1, rootsList)
    
    # return rootsList

    numberOfIslands = 0

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == "0": continue
            if isRoot(r * columns + c, rootsList): numberOfIslands += 1
    
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

print(numIslands([
    ["1","0","1","1","1"],
    ["1","0","1","0","1"],
    ["1","1","1","0","1"]])) 