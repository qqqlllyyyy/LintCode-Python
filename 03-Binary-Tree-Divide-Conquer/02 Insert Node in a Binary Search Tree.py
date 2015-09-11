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
    # Non-recursion
    
    def insertNode(self, root, node):
        # write your code here
        if root is None:
            return node
        
        cur = root
        while cur != node:
            if node.val < cur.val: # Attention: not "cur != None" !
                if cur.left is not None:
                    cur = cur.left
                else:
                    cur.left = node
                
            if node.val > cur.val:
                if cur.right is not None:
                    cur = cur.right
                else:
                    cur.right = node
                
        return root

    # Recursion
    
    def insertNode(self, root, node):
        if root == None: return node
        
        if node.val < root.val:
            if root.left == None:
                root.left = node
            else:
                self.insertNode(root.left, node)
        if node.val > root.val:
            if root.right == None:
                root.right = node
            else:
                self.insertNode(root.right, node)
        return root
