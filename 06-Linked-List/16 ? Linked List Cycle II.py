# Linked List Cycle II
# Given a linked list, return the node where the cycle begins. If there 
# is no cycle, return null.
#
# Example
# Given -21->10->4->5, tail connects to node index 1, return 10
#
# Challenge
# Can you solve it without using extra space?
#
# Explanation: http://www.cnblogs.com/zuoyuan/p/3701877.html

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
    @return: The node where the cycle begins. 
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if head == None or head.next == None:
            return None
            
        slow = head
        fast = head.next
        
        while fast != slow:
            if fast == None or fast.next == None:
                return None
            slow = slow.next
            fast = fast.next.next
        
        while head != slow.next: # Why?
            head = head.next
            slow = slow.next
        return head

