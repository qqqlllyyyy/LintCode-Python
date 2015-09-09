# Reverse Linked List
# Reverse a linked list.
#
# Example
# For linked list 1->2->3, the reversed linked list is 3->2->1
#
# Challenge
# Reverse it in-place and in one-pass
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
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.
    """
    def reverse(self, head):
        # write your code here
        curr = None
        
        while head != None:
            temp = head.next
            head.next = curr
            curr = head
            head = temp
            
        # Remember to return "curr", not "head"
        # Because after the "while" loop, "head" is None, curr is the last node.
        
        return curr
