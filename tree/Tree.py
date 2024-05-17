class Node:
        def __init__(self, data):
            self.data = data
            self.children = []

"""
create 
insert 
serach 
traveral
    depth
    breadth
"""

from collections import deque

# function to add an edge between vertices x and y
def addEdge(x,y,adj):
    adj[x].append(y)
    adj[y].append(x)

# function to print the parent of each node
def printParents(node, adj, parent):
    # current node is Root, thus, has no parent
    if parent == 0:
        print("{} -> Root".format(node))
    else:
        print("{}-> {}".format(node,parent))

