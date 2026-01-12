from a_star import Node, a_star

# Create 10 nodes arranged in a 2D grid
# 2   0 --- 1 --- 2
#     |     |     |
# 1   3 --- 4 --- 5
#     |     |     |
# 0   6 --- 7 --- 8
#           |
# -1        9

nodes = {
    0: Node("0", 0, 2),
    1: Node("1", 1, 2),
    2: Node("2", 2, 2),
    3: Node("3", 0, 1),
    4: Node("4", 1, 1),
    5: Node("5", 2, 1),
    6: Node("6", 0, 0),
    7: Node("7", 1, 0),
    8: Node("8", 2, 0),
    9: Node("9", 1, -1),
}

# Connect nodes with costs
edges = [
    (0, 1, 1), (1, 2, 1),
    (0, 3, 1), (1, 4, 1), (2, 5, 1),
    (3, 4, 1), (4, 5, 2),
    (3, 6, 1), (4, 7, 10), (5, 8, 1),
    (6, 7, 5), (7, 8, 1),
    (7, 9, 1),
]

for start_idx, end_idx, cost in edges:
    nodes[start_idx].add_neighbour(cost, nodes[end_idx])
    nodes[end_idx].add_neighbour(cost, nodes[start_idx])

# Test A* from node 0 to node 9
start = nodes[1]
end = nodes[9]

path, distance = a_star(start, end)

if path:
    path.reverse()
    print(f"Path found: {' -> '.join([node.name for node in path])}")
    print(f"Total distance: {distance}")
else:
    print("No path found")
