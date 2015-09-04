# Binary Tree Inorder Traversal
# Given a binary tree, return the inorder traversal of its nodes' values.
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
    @return: Inorder in ArrayList which contains node values.
    """
    
    # Iterative
    
    def inorderTraversal(self, root):
        result = []
        if root == None:
            return result
        
        stack = []
        cur = root
        while cur != None or len(stack) > 0:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
        
        return result
                
                
            
    # Recursive  
        
    def inorderTraversal(self, root):
        result = []
        self.helper(root, result)
        return result
        
        
    def helper(self, root, result):
        if root == None:
            return 
        
        self.helper(root.left, result)
        result.append(root.val)
        self.helper(root.right
