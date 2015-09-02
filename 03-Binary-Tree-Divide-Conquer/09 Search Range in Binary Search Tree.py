# Search Range in Binary Search Tree
# Given two values k1 and k2 (where k1 < k2) and a root pointer to a 
# Binary Search Tree. Find all the keys of tree in range k1 to k2. i.e. 
# print all x such that k1<=x<=k2 and x is a key of given BST. Return 
# all the keys in ascending order.
#
#
# For each node, search its leftside, then itself, then its rightside
# So that the result will be in ascending order
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
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """     
    def searchRange(self, root, k1, k2):
        result = []
        self.helper(root, k1, k2, result)
        return result
        
    def helper(self, root, k1, k2, result):
        if root == None:
            return
        if root.val > k1:
            self.helper(root.left, k1, k2, result)
        if k1 <= root.val <= k2:
            result.append(root.val)
        if root.val < k2:
            self.helper(root.right, k1, k2, result)
