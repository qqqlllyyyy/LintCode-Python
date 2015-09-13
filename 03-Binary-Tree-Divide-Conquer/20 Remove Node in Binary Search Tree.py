# Remove Node in Binary Search Tree
# Given a root of Binary Search Tree with unique value for each 
# node.  Remove the node with given value. If there is no such a 
# node with given value in the binary search tree, do nothing. You 
# should keep the tree still a binary search tree after removal.
#
# Example
# Given binary search tree:
#     5
#    / \
#   3   6
#  / \
# 2   4
# Remove 3, you can either return:
#    5        5
#   / \      / \
#  2   6 or 4   6
#   \      /
#    4    2
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
    @param value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """    
    def removeNode(self, root, value):
        # write your code here
        dummy = TreeNode(0)
        dummy.left = root
        
        parent = self.findNode(dummy, root, value)
        if parent.left != None and parent.left.val == value:
            node = parent.left
        elif parent.right != None and parent.right.val == value:
            node = parent.right
        else:
            return dummy.left
        
        self.deleteNode(parent, node)
        return dummy.left
        
    # Find the parent of the node with "node.val = value"
    def findNode(self, parent, node, value):
        if node == None: return parent
        if node.val == value: return parent
        
        if value < node.val:
            return self.findNode(node, node.left, value)
        if value > node.val:
            return self.findNode(node, node.right, value)
    
    # Delete the node
    def deleteNode(self, parent, node):
        
        if node.right == None:
            
            if parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left
        
        else:
            temp = node.right
            father = node
            while temp.left != None: # Find the smallest value larger than node.val
                father = temp
                temp = temp.left
            
            if father.left == temp:
                father.left = temp.right
            else:
                father.right = temp.right
            
            if parent.left == node:
                parent.left = temp
            else:
                parent.right = temp
            
            temp.left = node.left
            temp.right = node.right

        
        

