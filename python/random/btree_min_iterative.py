class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

a = Node(5)
b = Node(6)
c = Node(2)
d = Node(8)
e = Node(8)
f = Node(10)

#a = Node('a')
#b = Node('b')
#c = Node('c')
#d = Node('d')
#e = Node('e')
#f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def minTree(root : Node):
    queue = [root]
    currMin = root.value
    while(len(queue) > 0):
        current =  queue.pop(0)
        if current.left != None: queue.append(current.left)
        if current.right != None: queue.append(current.right)
        if current.value < currMin: currMin = current.value
    return currMin

print(minTree(a))
