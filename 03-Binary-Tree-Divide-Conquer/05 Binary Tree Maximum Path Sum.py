# Binary Tree Maximum Path Sum
# Given a binary tree, find the maximum path sum.
# The path may start and end at any node in the tree.
#
# => Max Path
# 1. The path contains at least one node
# 2. Value of node can < 0
# 3. From any node to any node
#
# => Simple Path
# 1. The path can contain no node
# 2. value of node can < 0
# 3. From root to any node
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
    def maxPathSum(self, root):
        maxSum, _ = self.maxPathHelper(root)
        return maxSum
        
    def maxPathHelper(self, root):
        if root is None:
            return -sys.maxint, 0
        
        left = self.maxPathHelper(root.left)
        right = self.maxPathHelper(root.right)
        maxpath = max(left[0], right[0], root.val + left[1] + right[1])
        single = max(left[1] + root.val, right[1] + root.val, 0) # Don't forget 0 here !
        
        return maxpath, single
