def pacificAtlantic(heights: "list[list[int]]") -> "list[list[int]]":
    # base case:
    if heights[0] == []:
        return 0
    
    # save dimentions
    rows = len(heights)
    columns = len(heights[0])

    atlantic, pacyfic = set(), set()

    def depth_first_search(row : 'int', column : 'int', visited : "set", previous_height : "int") -> None:
        if row < 0 or row >= rows or column < 0 or column >= columns or (row,column) in visited or previous_height > heights[row][column]:
            return

        visited.add((row,column))

        depth_first_search (row - 1, column, visited, heights[row][column])
        depth_first_search (row + 1, column, visited, heights[row][column])
        depth_first_search (row, column - 1, visited, heights[row][column])
        depth_first_search (row, column + 1, visited, heights[row][column])

    for column in range(columns):
        depth_first_search(0, column, pacyfic, heights[0][column])
        depth_first_search(rows - 1, column, atlantic, heights[rows - 1][column])

    for row in range(rows):
        depth_first_search(row, 0, pacyfic, heights[row][0])
        depth_first_search(row, columns - 1, atlantic, heights[row][columns - 1])
    
    result = []
    for pair in pacyfic:
        if pair in atlantic:
            result.append([pair[0], pair[1]])
        
    return result


# print (pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
# print (pacificAtlantic([[2,1],[1,2]]))
