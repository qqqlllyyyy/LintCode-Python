# Binary Tree Level Order Traversal
# Given a binary tree, return the level order traversal of its nodes' 
# values. (ie, from left to right, level by level).
#
# Example
#    3
#   / \
#  9  20
#    /  \
#   15   7
# return its level order traversal as:
# [[3], [9,20], [15,7]]


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
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        result = []
        if root == None:
            return result
        
        toBeProcessed = [root]
        while toBeProcessed:
            A = [] # A contains values
            B = [] # B contains nodes
            for node in toBeProcessed:
                A.append(node.val)
                if node.left != None:
                    B.append(node.left)
                if node.right != None:
                    B.append(node.right)
            toBeProcessed = B # ? Why the change on B will not automatically change toBeProcessed?
            result.append(A)
        return result
                
                
    # ? One Queue Implementation?
