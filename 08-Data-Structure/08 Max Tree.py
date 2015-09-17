# Max Tree
# Given an integer array with no duplicates. A max tree building on
# this array is defined as follow:
# 1. The root is the maximum number in the array
# 2. The left subtree and right subtree are the max trees of the 
#    subarray divided by the root number.
# Construct the max tree by the given array.
#
# Example
# Given [2, 5, 6, 0, 3, 1], the max tree constructed by this array is:
#      6
#     / \
#    5   3
#   /   / \
#  2   0   1 
#
# Challenge
# O(n) time and memory.

"""Is this O(n)?"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
        
class Solution:
    
    def maxTree(self, A):
        list = []
        for element in A:
            node = TreeNode(element)
            # For a new node, push it to the left so that all the 
            # nodes to its left have larger values.
            while len(list) > 0 and element > list[len(list) - 1].val:
                node.left = list.pop() # Biggest node is the first one
            if len(list) > 0:
                list[len(list) - 1].right = node
            list.append(node)
        return list[0]
                

# If I define a Stack first. Read this and remember how to define a stack        
class Stack:
  def __init__(self):
    self.items = []

  def __getitem__(self, index):
    return self.items[index]

  def isEmpty(self):
    return len(self.items)==0
   
  def push(self, item):
    self.items.append(item)
   
  def pop(self):
    return self.items.pop() 
   
  def peek(self):
    if not self.isEmpty():
      return self.items[len(self.items)-1]
     
  def size(self):
    return len(self.items) 
    
class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
        # write your code here
        stk = Stack()
        for ele in A:
            node = TreeNode(ele)
            while not stk.isEmpty() and ele > stk.peek().val:
                node.left = stk.pop()
            if not stk.isEmpty():
                stk.peek().right = node
            stk.push(node)
        return stk[0]
        
