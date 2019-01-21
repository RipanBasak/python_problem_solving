
class Node:
    #initialize node
    def __init__(self, value):
        self.value =  value
        # self.parent = None
        self.left = None
        self.right = None

#find the parent path

def findPath( parent, path, value):

    if parent is None:
        return False

    path.append(parent.value)

    if parent.value == value :
        return True

    if ((parent.left != None and findPath(parent.left, path, value)) or
            (parent.right!= None and findPath(parent.right, path, value))):
        return True



    path.pop()
    return False

#lca logic
def findLCA(parent, n1, n2):

    path1 = []
    path2 = []

    if (not findPath(parent, path1, n1) or not findPath(parent, path2, n2)):
        return -1

    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]


#initialize parent, left and right node
parent = Node(1)
parent.left = Node(2)
parent.right = Node(3)
parent.left.left = Node(4)
parent.left.right = Node(5)
parent.right.left = Node(6)
parent.right.right = Node(7)
parent.left.left = Node(8)
parent.left.right = Node(9)

def lca(node1, node2):
    print (findLCA(parent, node1, node2))

#call lca
lca(6, 7)



