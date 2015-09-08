# Remove Nth Node From End of List
# Given a linked list, remove the nth node from the end of list and return its head.
#
# Example
# Given linked list: 1->2->3->4->5->null, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5->null.
#
# Note
# The minimum number of nodes in list is n.
#
# Challenge
# O(n) time

"""Explanation: http://www.cnblogs.com/zuoyuan/p/3701971.html"""
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        
        if n <= 0:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy
        for i in range(n):
            p1 = p1.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummy.next
