# Partition List
# Given a linked list and a value x, partition it such that all nodes less 
# than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each 
# of the two partitions.
#
# Example
# Given 1->4->3->2->5->2->null and x = 3,
# return 1->2->2->4->3->5->null.
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
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        # write your code here
        if head == None:
            return None
        leftDummy = ListNode(0)
        rightDummy = ListNode(0)
        # Note you can not write:
        # "leftDummy = rightDummy = ListNode(0)" here
        
        left, right = leftDummy, rightDummy
        
        while head != None:
            if head.val < x:
                left.next = head
                left = head
            else:
                right.next = head
                right = head
            head = head.next
            
        right.next = None
        left.next = rightDummy.next
        return leftDummy.next
