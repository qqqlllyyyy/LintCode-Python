# Lowest Common Ancestor
# Given the root and two nodes in a Binary Tree. Find the lowest 
# common ancestor(LCA) of the two nodes.
# The lowest common ancestor is the node with largest depth which 
# is the ancestor of both nodes.
#
#
#
# Find LCA of A,B in the binary tree whose root is 'root'
# If we find this LCA, return it
# If we find A only, then return A
# If we find B only, return B
# If we find neither A nor B, return 'None'
#

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """ 
    def lowestCommonAncestor(self, root, A, B):
        
        if root == None or root == A or root == B:
            return root
            
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)
        
        if left != None and right!= None:
            return root
            
        if left != None:
            return left
        
        if right != None:
            return right
            
        else:
            return None
