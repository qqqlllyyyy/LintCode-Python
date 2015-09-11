# Insert Node in a Binary Search Tree
# Given a binary search tree and a new tree node, insert the node 
# into the tree. You should keep the tree still be a valid binary 
# search tree.
#
# Challenge
# Can you do it without recursion?
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
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if root is None:
            return node
        
        cur = root
        while cur != node: # Attention: not "cur != None" !
            if node.val < cur.val:
                if cur.left is not None:
                    cur = cur.left
                else:
                    cur.left = node  # Can not use "node = cur.left"
                
            if node.val > cur.val:
                if cur.right is not None:
                    cur = cur.right
                else:
                    cur.right = node
                
        return roo
        ## How to do it with recursion? 
