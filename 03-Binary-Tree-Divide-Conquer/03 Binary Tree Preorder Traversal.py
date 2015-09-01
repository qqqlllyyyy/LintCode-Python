# Binary Tree Preorder Traversal
# Given a binary tree, return the preorder traversal of its nodes' values.
#
# Challenge
# Can you do it without recursion?
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
    @return: Preorder in ArrayList which contains node values.
    """
## Without Recursion
    def preorderTraversal(self, root):
        if root is None:
            return []
        
        stack = [root]
        preorder = []
        
        while len(stack) > 0:
            node = stack.pop()
            preorder.append(node.val)
            
            # First 'right', and then 'left'
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return preorder


## With Recursion
      
    def preorderTraversal(self, root):

        result = []
        self.traverse(root, result)
        return result
        
    def traverse(self, root, result):
        if root == None:
            return
