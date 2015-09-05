# Construct Binary Tree from Inorder and Postorder Traversal
# Given inorder and postorder traversal of a tree, construct the binary tree.
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
    @param inorder : A list of integers that inorder traversal of a tree
    @param postorder : A list of integers that postorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, inorder, postorder):
       
        if not inorder:
            return None
        
        root = TreeNode(postorder[len(postorder) - 1])
        rootPos = inorder.index(postorder[len(postorder) - 1])
        
        root.left = self.buildTree(inorder[: rootPos], postorder[: rootPos])
        root.right = self.buildTree(inorder[rootPos + 1 : ], postorder[rootPos: len(postorder) - 1])
        return root
