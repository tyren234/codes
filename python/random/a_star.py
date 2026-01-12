import heapq
import math
class Node:
    def __init__(self, name, x, y):
        self.neighbours = set()
        self.name = name
        self.x = x
        self.y = y
        self.distance = float("inf")
        self.prev = None
    def add_neighbour(self, cost: int, node) -> None:
        self.neighbours.add((cost, node))
    def heuristic(self, goal) -> int:
        # sqrt(a^2 + b^2) = c
        return math.sqrt(pow(abs(goal.x - self.x),2) + pow(abs(goal.y - self.y),2))
    def __lt__(self, other):
        return self.distance < other.distance


def a_star(start: Node, end: Node) -> tuple[list[Node], int]:
    # we prioritize minimum distance + heuristic
    start.distance = 0
    queue = []
    f = start.distance + start.heuristic(end)
    heapq.heappush(queue, (f, start))
    while queue:
        _, current = heapq.heappop(queue)
        for cost, neighbour in current.neighbours:
            if neighbour is end:
                end.prev = current
                end.distance = current.distance + cost
                queue.clear()
                break
            if current.distance + cost < neighbour.distance:
                neighbour.prev = current
                neighbour.distance = current.distance + cost
                f = neighbour.distance + neighbour.heuristic(end)
                heapq.heappush(queue, (f, neighbour))
    if end.distance != float("inf"):
        path = []
        node = end
        while node is not None:
            path.append(node)
            node = node.prev
        return (path, end.distance)
    return ([], -1)



            
