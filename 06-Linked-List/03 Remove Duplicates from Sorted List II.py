# Remove Duplicates from Sorted List II
# Given a sorted linked list, delete all nodes that have duplicate 
# numbers, leaving only distinct numbers from the original list.
#
# Example
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
#
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
        
        if head == None or head.next == None:
            return None
            
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        
        while head.next != None and head.next.next != None:
            if head.next.val == head.next.next.val:
                value = head.next.val
                # use 'while' here, not 'if'
                
                while head.next != None and head.next.val == value:
                    # Can not remove 'head.next != None' here!
                    # Because if head.next == None, it doesn't have '.val' attr
                    head.next = head.next.next
            else:
                head = head.next
        
        return dummy.next
                
            
