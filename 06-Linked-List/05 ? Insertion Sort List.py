# Insertion Sort List
# Sort a linked list using insertion sort.
#
# Example
# Given 1->3->2->0->null, return 0->1->2->3->null.
#
#
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
    @return: The head of linked list.
    """
    # Easy to understand
    
    def insertionSortList(self, head):
        
        dummy = ListNode(0)
        
        while head != None:
            node = dummy
            while node.next != None and node.next.val < head.val:
                node = node.next
                
            temp = head.next
            head.next = node.next
            node.next = head # Pay attention to the order here !
            
            head = temp
    
        return dummy.next


    # Good Method (don't quite understand)
    
    def insertionSortList(self, head):
        
        pre = cursor = dummy_head = ListNode(0)
        dummy_head.next = head

        while cursor.next:
            if pre.next.val > cursor.next.val:
                pre = dummy_head

            while pre.next.val < cursor.next.val:
                pre = pre.next

            if pre != cursor:
                node = cursor.next
                cursor.next = node.next
                node.next = pre.next
                pre.next = node
            else:
                cursor = cursor.next

        return dummy_head.next
            
                
            
