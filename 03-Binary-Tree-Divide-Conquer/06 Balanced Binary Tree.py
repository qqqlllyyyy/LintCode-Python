# Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as a binary 
# tree in which the depth of the two subtrees of every node never differ 
# by more than 1.
#
# Note:
# A root is necessary for this problem
#

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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        balanced, height = self.validate(root)
        return balanced


    # return two results: whether it's balanced, maxHeight
    def validate(self, root):
        if root == None:
            return True, 0

        # Since we need the tree to be balanced for every node
        # So if for some node, it's unbalanced, we can return False
        # for all its ancestors
        left = self.validate(root.left)
        if left[0] == False:
            return False, 0 # Doesn't matter which number to follow
        
        right = self.validate(root.right)
        if right[0] == False:
            return False, 0
            
        return abs(left[1] - right[1]) <= 1, max(left[1], right[1]) + 1
