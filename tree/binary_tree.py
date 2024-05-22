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


class Stack:
    def __init__(self,capacity):
        self.size = 0
        self.capacity = capacity
        self.array = [None] * capacity

    def push(self,value):
        if self.isFull():
            raise Exception('tree is full')
        self.array[self.size] = value
        self.size += 1
    def pop(self):
        if self.isEmpty():
            raise Exception('tree is empty')
        temp = self.array[self.size-1]
        self.size -= 1
        return temp
    def peek(self):
        if self.isEmpty():
            raise Exception('tree is empty')
        return self.array[self.size-1]

    def isFull(self):
        return self.size == self.capacity
    def isEmpty(self):
        return self.size == 0

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val


#         TODO deque must to learn it
# https://www.geeksforgeeks.org/introduction-to-binary-tree-data-structure-and-algorithm-tutorials/
from stack import stack_demo


def printPreOrderByRecursion(node):
    if node is None:
        return
    print(node.data, end=" ")
    # Recursion to process
    printPreOrderByRecursion(node.left)
    printPreOrderByRecursion(node.right)


def printPreOrderByIterative(node):
    stack = Stack(20)
    if node is None:
        return

    #       1
    #     /   \
    #    2     3
    #  /   \     \
    # 4     5     6

    while node is not None or (not stack.isEmpty()):
        if node is not None:
            print(node.data, end=" ")
            stack.push(node)
            node = node.left
        elif not stack.isEmpty():
            print("开始弹栈")
            node = stack.pop()
            if node.right is not None:
                node = node.right
                print(node.data, end=" ")
                node = node.left


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    print("PreOrder traversal of binary tree is:")
    printPreOrderByRecursion(root)
    printPreOrderByIterative(root)
