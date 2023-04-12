class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
def cloneGraph(node : 'Node') -> 'Node':
    oldToNew = dict()

    def cloneNode (node : 'Node') -> 'Node':
        '''
        Clones the node and returns it's clone. 
        Also sets up connections i.e. if original node A is connected to node B then clone A' will be connected to cloned B'
        '''
        if node in oldToNew:
            return oldToNew[node]

        clone = Node(node.val)
        oldToNew[node] = clone

        for neighbor in node.neighbors:
            if neighbor in oldToNew:
                clone.neighbors.append(oldToNew[neighbor])
            else:
                clone.neighbors.append(cloneNode(neighbor))
        
        return clone
    
    return cloneNode(node) if node else None
