# Binary Tree Level Order Traversal II
# Given a binary tree, return the bottom-up level order traversal of its 
# nodes' values. (ie, from left to right, level by level from leaf to root).
#
# Example
# Given binary tree {3,9,20,#,#,15,7},
#   3
#  / \
# 9  20
#   /  \
#  15   7
# return its bottom-up level order traversal as:
# [
#  [15,7],
#  [9,20],
#  [3]
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
    @return: buttom-up level order in a list of lists of integers
    """
    # Non-recursion
    def levelOrderBottom(self, root):
        result = []
        if root == None: return result
        A = [root]
        B = []
        while len(A) > 0:
            currentResult = []
            while len(A) > 0: # Think again.
                node = A.pop(0) # Get the first one.
                currentResult.append(node.val)
                if node.left != None: B.append(node.left)
                if node.right != None: B.append(node.right)
            result.insert(0, currentResult)
            A = B
            B = []
        return result
    
    # Recursion
    def levelOrderBottom(self, root):
        result = []
        self.helper(root, 0, result)
        result1 =self.reverse(result)
        return result1
        
    def helper(self, root, level, result):
        if root == None: return
        if len(result) < level + 1:
            result.append([])
        result[level].append(root.val)
        self.helper(root.left, level + 1, result)
        self.helper(root.right, level + 1, result)
    
    def reverse(self, list0):
        list1 = []
        if len(list0) == 0: return list1
        while list0:
            node = list0.pop()
            list1.append(node)
        return list1
        
        
        
