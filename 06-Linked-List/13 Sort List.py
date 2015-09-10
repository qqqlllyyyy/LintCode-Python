# Sort List
# Sort a linked list in O(n log n) time using constant space complexity.
#
# Example
# Given 1-3->2->null, sort it to 1->2->3->null.
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
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    """
        Use Merge Sort !
    """
    
    # Finde the middle node
    def findMiddle(self, head):
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    # Merge two lists in ascending order
    def merge(self, list1, list2):
        dummy = ListNode(0)
        node = dummy
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        
        if list1 != None:
            node.next = list1
        else:
            node.next = list2
        
        return dummy.next
    
    
    def sortList(self, head):
        # write your code here
        if head == None or head.next == None:
            return head
        
        mid = self.findMiddle(head)
        
        # Pay attention to the order here
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        
        return self.merge(left, right)
        
