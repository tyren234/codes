class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def LookingFor(root, target):
    if root == None: return False
    if root.value == target: return True
    return (LookingFor(root.left, target) or LookingFor(root.right, target))

print(LookingFor(a,'k'))
