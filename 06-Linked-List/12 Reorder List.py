# Reorder List
# Given a singly linked list L: L(0)->L(1)->L(2)-> ... ->L(n)
# reorder it to: L(0)->L(n)->L(1)->L(n-1)->L(2)->L(n-2)-> ...
# You must do this in-place without altering the nodes' values.
#
# Example
# Given 1->2->3->4->null, reorder it to 1->4->2->3->null.


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
    @return: nothing
    """
    """
        First we find the middle of the list, reverse the second part.
        Then merge those two lists to get what we want
    """
    
    # Reverse a list
    def reverse(self, head):
        curr = None # Not head !
        while head != None:
            temp = head.next
            head.next = curr
            curr = head
            head = temp
        return curr
    
    # Merge two lists
    def merge(self, list1, list2):
        dummy = ListNode(0)
        index = 0
        while list1 != None and list2 != None:
            if index % 2 == 0:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
            index += 1
        if list1 != None:
            dummy.next = list1
        else:
            dummy.next = list2
    
    # Find the middle node
    def findMiddle(self, head):
        slow = head
        fast = head.next
        while fast != None and fast.next != None: # Use "if" by mistake
            slow = slow.next
            fast = fast.next.next
        return slow
                
    # Final step
    def reorderList(self, head):
        # write your code here
        if head == None or head.next == None:
            return 
        mid = self.findMiddle(head)
        tail = self.reverse(mid.next) # Note here is "mid.next", not "mid"!
        mid.next = None # Don't forget this step !!
        self.merge(head, tail)
