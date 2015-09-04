# Minimum Depth of Binary Tree
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest 
# path from the root node down to the nearest leaf node.
#
#
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
    @return: An integer
    """ 
    def minDepth(self, root):
        # write your code here
        if root == None:
            return 0
        
        if root.left == None and root.right != None:
            return self.minDepth(root.right) + 1
        if root.right == None and root.left != None:
            return self.minDepth(root.left) + 1
            
        return min( self.minDepth(root.left), self.minDepth(root.right) ) + 1
