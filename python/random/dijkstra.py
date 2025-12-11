import copy
import heapq

class Node:
    def __init__(self, name):
        self.name = name
        self.costs = {}
        self.distance = float('inf')
    def __lt__(self, other):
        return self.distance < other.distance
    def __eq__(self, other):
        return self.name == other.name and self.costs == other.costs
    def __hash__(self):
        return hash(self.name)

def add_neighbor(node_from, node_to, cost):
    node_from.costs[node_to] = cost
    node_to.costs[node_from] = cost    

def dijkstra(nodes, start, end) -> int:
    start.distance = 0
    queue = []    
    current = start
    while(current.name is not end.name):
        # print()
        # print(f"Current {current.name}")
        for neighbor in current.costs.keys():
            # print(f"Neigbor {neighbor.name}")
            if current.costs[neighbor] + current.distance < neighbor.distance:
                neighbor.distance = current.costs[neighbor] + current.distance
                heapq.heappush(queue, (neighbor.distance, neighbor))
                # print(f"Pushing {neighbor.name} with dist {neighbor.distance}. Queue {[(dist, node.name) for (dist, node) in queue]}")

        if len(queue) == 0:
            # print(f"Processed all and didn't find the end")
            break
        (_, current) = heapq.heappop(queue)
        # print(f"Retreived {current.name} {_}")

    return end.distance


# A = Node("A")
# B = Node("B")
# C = Node("C")
# D = Node("D")
# nodes = {A, B, C, D}
# add_neighbor(A, B, 5)
# add_neighbor(A, C, 2)
# add_neighbor(B, D, 1)
# add_neighbor(C, D, 1)   
# output = dijkstra(nodes, A, D)


# More complex graph:
#         A (start)
#        / \
#       1   4
#      /     \
#     B---2---C
#     |       |
#     3       2
#     |       |
#     D---1---E (end)
#
# Shortest paths from A to E:
# A->B(1)->C(2)->E(2) = 5
# A->B(1)->D(3)->E(1) = 5
# A->C(4)->E(2) = 6
# Expected shortest distance: 5

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
nodes = {A, B, C, D, E}

add_neighbor(A, B, 1)
add_neighbor(A, C, 4)
add_neighbor(B, C, 2)
add_neighbor(B, D, 3)
add_neighbor(C, E, 2)
add_neighbor(D, E, 1)

output = dijkstra(nodes, A, E)
print(output)