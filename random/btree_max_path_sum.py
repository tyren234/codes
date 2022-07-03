import math
class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(2)
f = Node(1)

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

def maxPathSum(root : Node):
    if root == None: return -math.inf
    if root.left == None and root.right == None: return root.value
    return root.value + max(maxPathSum(root.left), maxPathSum(root.right))

print(maxPathSum(a))
