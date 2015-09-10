# Rotate List
# Given a list, rotate the list to the right by k places,
# where k is non-negative.
#
# Example
# Given 1->2->3->4->5 and k = 2, return 4->5->1->2->3.
#
#
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    
    # Get the length first
    def getLength(self, head):
        length = 0
        while head != None:
            head = head.next
            length += 1
        return length
    
    
    def rotateRight(self, head, k):
        # write your code here
        if head == None: return None
        length = self.getLength(head)
        k = k % length
        
        dummy = ListNode(0)
        dummy.next = head
        head = dummy

        tail = dummy        
        for i in range(k):
            head = head.next
        
        while head.next != None:
            tail = tail.next
            head = head.next
        
        head.next = dummy.next
        dummy.next = tail.next
        tail.next = None
        
        return dummy.next
        
        

