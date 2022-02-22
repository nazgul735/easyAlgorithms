from distutils.log import error

class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        # tree direction (0/1)
        self.huff = ''
def printNodes(node, val=''):
    newVal = val + str(node.huff)
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)
        # if node is edge node then
        # display its huffman code
    print(f"{node.symbol} -> {newVal}") if(not node.left and not node.right) else None 
# characters for huffman tree
chars = ['a', 'b', 'c', 'd', 'e', 'f']
# frequency of characters
freq = [ 5, 9, 12, 13, 16, 45]
# list containing unused nodes
nodes = []
# converting characters and frequencies
# into huffman tree nodes
for x in range(len(chars)):
    nodes.append(node(freq[x], chars[x]))
while len(nodes) > 1:
    # sort all the nodes in ascending order
    # based on theri frequency
    nodes = sorted(nodes, key=lambda x:x.freq)
    # pick 2 smallest nodes
    left = nodes[0]
    right = nodes[1]
    # assign directional value to these nodes
    left.huff = 0
    right.huff = 1
    # combine the 2 smallest nodes to create
    # new node as their parent
    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
    # remove the 2 nodes and add their
    # parent as new node among others
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)
# Huffman Tree is ready!
printNodes(nodes[0])
    



# printTree(node.left or node.right, newVal) if(node.left or node.right) else print(f"{node.symbol} -> {newVal}"
