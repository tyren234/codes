def uniquePaths(m: int, n: int) -> int:
    # m - rows, n - columns
    # initialise
    grid = [[0 for j in range(n+1)] for i in range(m+1)]
    grid[m][n-1] = 1

    # all the work
    for i in reversed(range(m)):
        for j in reversed(range(n)):
            grid[i][j] = grid[i+1][j] + grid[i][j+1]
    
    # return
    return grid[0][0]

print(uniquePaths(3,7))