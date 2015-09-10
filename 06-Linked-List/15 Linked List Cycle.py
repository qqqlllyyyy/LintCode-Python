# Linked List Cycle
# Given a linked list, determine if it has a cycle in it.
#
# Example
# Given -21->10->4->5, tail connects to node index 1, return true
#
# Challenge
# Can you solve it without using extra space?
#
# Explanation: http://www.cnblogs.com/zuoyuan/p/3701639.html
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
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if head == None or head.next == None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

