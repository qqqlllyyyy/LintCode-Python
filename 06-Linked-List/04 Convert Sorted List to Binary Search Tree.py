# Convert Sorted List to Binary Search Tree
# Given a singly linked list where elements are sorted in ascending 
# order, convert it to a height balanced BST.
#
# Example
#               2
# 1->2->3  =>  / \
#             1   3
#

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    # Translate the List to an Array first
    # Then use the function "sortedArrayToBST", which is another problem.
    
    def sortedListToBST(self, head):
        array = []
        while head != None:
            array.append(head.val)
            head = head.next
        return self.sortedArrayToBST(array)
            

    def sortedArrayToBST(self, array):
        length = len(array)
        if length == 0: return None
        if length == 1: return TreeNode(array[0])
        root = TreeNode(array[length / 2])
        root.left = self.sortedArrayToBST(array[ : length / 2])
        root.right = self.sortedArrayToBST(array[length / 2 + 1 : ])
        return root
        

