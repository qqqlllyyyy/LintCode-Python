# Inorder Successor in BST
# Given a binary search tree and a node in it, find the in-order
# successor of that node in the BST.
#
# Example
# Given tree = [2,1] and node = 1:
#   2
#  /
# 1      return node 2.
#
# Note
# If the given node has no in-order successor in the tree, return null.
# Challenge
# O(h), where h is the height of the BST.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if root == None: return None
        
        result = None
        while root.val != None and root.val != p.val:
            if p.val < root.val:
                result = root
                root = root.left
            else:
                root = root.right
        
        if root == None: 
            return None
        if root.right == None:
            return result
        
        root = root.right
        while root.left != None:
            root = root.left
        return root
