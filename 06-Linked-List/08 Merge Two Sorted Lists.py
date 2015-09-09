# Merge Two Sorted Lists
# Merge two sorted (ascending) linked lists and return it as a new 
# sorted list. The new sorted list should be made by splicing 
# together the nodes of the two lists and sorted in ascending order.
#
# Example
# Given 1->3->8->11->15->null, 2->null 
# return 1->2->3->8->11->15->null.
#
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        
        dummy = ListNode(0)
        lastNode = dummy
        
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                lastNode.next = l1
                l1 = l1.next
            else:
                lastNode.next = l2
                l2 = l2.next
            lastNode = lastNode.next
            
        if l1 != None: # Don't need 'while' here because nodes afterwards
        # have been linked already
            lastNode.next = l1
        else:
            lastNode.next = l2
        
        return dummy.next

