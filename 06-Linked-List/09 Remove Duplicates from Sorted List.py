# Remove Duplicates from Sorted List
# Given a sorted linked list, delete all duplicates such that each 
# element appear only once.
#
# Example
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.
#
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
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head == None:
            return None
            
        node = head
        while node.next != None:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        
        return head
