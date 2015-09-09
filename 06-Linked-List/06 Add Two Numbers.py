# Add Two Numbers
# You have two numbers represented by a linked list, where each 
# node contains a single digit. The digits are stored in reverse
# order, such that the 1's digit is at the head of the list. Write a 
# function that adds the two numbers and returns the sum as a 
# linked list.
#
# Example
# Given 7->1->6 + 5->9->2. That is, 617 + 295.
# Return 2->1->9. That is 912.
# Given 3->1->5 and 5->9->2, return 8->0->8.
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2 
    def addLists(self, l1, l2):
        # write your code here
        if l1 == None or l2 == None:
            return None
        
        head = ListNode(0)
        point = head
        
        carry = 0 
        while l1 != None and l2 != None:
            sum = carry + l1.val + l2.val
            carry = sum / 10
            point.next = ListNode(sum % 10)
            l1 = l1.next
            l2 = l2.next
            point = point.next
        
        while l1 != None:
            sum = carry + l1.val
            carry = sum / 10
            point.next = ListNode(sum % 10)
            l1 = l1.next
            point = point.next
        
        while l2 != None:
            sum = carry + l2.val
            point.next = ListNode(sum % 10)
            carry = sum / 10
            l2 = l2.next
            point = point.next
        
        if carry != 0: # Don't forget this. You may have an "1" left.
            point.next = ListNode(carry)
        
        return head.next
