def numIslands(grid: 'list[list[str]]') -> int:
    rows = len(grid)
    columns = len(grid[0])
    # ids will be attributed to every item from 0 to rows*columns - 1 in ascending order.
    # example: rows = 3, columns = 2
    # ids: 0 1
    #      2 3
    #      4 5
    def getRoot(node, ):