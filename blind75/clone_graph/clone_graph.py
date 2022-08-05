class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
def cloneGraph(node: 'Node') -> 'Node':
        oldToNew = dict()

        def cloneTheNode(node : 'Node'):
            # already made a clone of it
            if node in oldToNew:
                return oldToNew[node]
            
            # a clone doesn't exist
            # make a clone
            clone = Node(node.val)
            # save a refference to the clone in our dictionary (oldOriginalNode -> cloneNode)
            oldToNew[node] = clone 
            
            # save our clone's neighbors (copy them from original node).
            # If proper neighbor isn't cloned yet then clone it and do the same for it - clone all their neighbors. 
            # But wait! There is such a fuction that returns clone of a given old node or, if no such clone exists, clones a node and sets it up. 
            # Yes...
            # Yes!
            # It is the exact same function! RECURSION!! 
            for neighbor in node.neighbors:
                clone.neighbors.append(cloneTheNode(neighbor))
            
            #return the already set up clone
            return clone

        return cloneTheNode(node) if node else None