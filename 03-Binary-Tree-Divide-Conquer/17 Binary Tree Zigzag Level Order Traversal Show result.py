# Binary Tree Zigzag Level Order Traversal
# Given a binary tree, return the zigzag level order traversal of its 
# nodes' values. (ie, from left to right, then right to left for the next 
# level and alternate between).
#
# Example
# Given binary tree:
#   3
#  / \
# 9  20
#   /  \
#  15   7
# return its zigzag level order traversal as:
# [
#  [3],
#  [20,9],
#  [15,7]
# ]
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: A list of list of integer include 
             the zig zag level order traversal of its nodes' values
    """
    # Recursion
    def zigzagLevelOrder(self, root):
        result = []
        self.helper(root, 0, result)
        return result
    
    def helper(self, root, level, result):
        if root == None: return
    
        if len(result) < level + 1:
            result.append([])
            
        if level % 2 == 0:
            result[level].append(root.val)
        else:
            result[level].insert(0, root.val)
        self.helper(root.left, level + 1, result)
        self.helper(root.right, level + 1, result)
        
    # Non-recursion. Understand!
    def zigzagLevelOrder(self, root):
        result = []
        if root == None: return result
        A = [root] # A and B are lists of TreeNodes
        B = []
        normalOrder = True
        
        while len(A) > 0:
            currentResult = [] # Need this because it's list of values
            while len(A) > 0:
                node = A.pop()
                currentResult.append(node.val)
                
                if normalOrder:
                    if node.left != None: B.append(node.left)
                    if node.right != None: B.append(node.right)
                else:
                    if node.right != None: B.append(node.right)
                    if node.left != None: B.append(node.left)
            
            result.append(currentResult)
            normalOrder = not normalOrder
            A = B
            B = []
        return result
            
            
    
            
    
    
    
    
    
        
