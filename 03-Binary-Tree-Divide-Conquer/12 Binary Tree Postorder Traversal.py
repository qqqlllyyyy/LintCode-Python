# Binary Tree Postorder Traversal
# Given a binary tree, return the postorder traversal of its nodes' values.
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
    @return: Postorder in ArrayList which contains node values.
    """
    # Iterative
    
    def postorderTraversal(self, root):
        result = []
        if root == None:
            return result
        
        stack = [root]
        prev = None
        while stack:
            cur = stack[len(stack) - 1]
            # Can not use "cur = stack.pop()" here because if cur has
            # children, cur should keep in stack. We can only get cur
            # out from "stack" and put it into "result" only if:
            # 1. it's left child and right child are both "None"
            # 2. it's left child and right child are been put in "result"
            
            if prev == None or prev.left == cur or prev.right == cur:
                if cur.left != None:
                    stack.append(cur.left)
                elif cur.right != None:
                    stack.append(cur.right)
                else:
                    result.append(cur.val)
                    stack.pop()
                    
            elif prev == cur.left:# Have to use "elif" here since prev may
                # be "None" and cur.left may also be "None". Then this
                # "if" and the previous "if" will both be executed.
                if cur.right != None:
                    stack.append(cur.right)
                    
            else:
                result.append(cur.val)
                stack.pop()
                
            prev = cur
            
        return result
            
        
       
    # Recursive
    
    def postorderTraversal(self, root):
        result = []
        self.helper(root, result)
        return result
        
    def helper(self, root, result):
        if root == None:
            return 
        
        self.helper(root.left, result)
        self.helper(root.right, result)
        result.append(root.val)
        
        return
        
