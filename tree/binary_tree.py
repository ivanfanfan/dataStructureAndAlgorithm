"""
type of binary tree
    on the basis of Number of Children
        full binary tree
        degenerate binary tree
        skewed binary tree
    on the basis of Completion of levels
        complete Binary Tree
        Perfect Binary Tree
        Balanced Binary Tree
    on the basis of Node Values
        Binary Search Tree
        AVL Tree
        B Tree
        B+ Tree
        Segment Tree

Traversal of binary tree
    Depth-First
        Preorder traversal
        Inorder traversal
        postorder traversal

    Breadth-First
        Level Order Traversal: visit nodes level-by-level and
        left-to-right fashion at the same level.
"""
from collections import deque

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

    def insert(root, data):
        if root is None:
            root = Node(data)
            return root
#         TODO deque must to learn it
# https://www.geeksforgeeks.org/introduction-to-binary-tree-data-structure-and-algorithm-tutorials/











