# Merge k Sorted Lists
# Merge k sorted linked lists and return it as one sorted list.
# Analyze and describe its complexity.
#
# Example
# Given lists:
# [
#   2->4->null,
#   null,
#   -1->null
# ],
# return -1->2->4->null.
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
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        # Something like merge sort, divide and conquer.
        if len(lists) == 0:
            return None
        return self.helper(lists, 0, len(lists) - 1)
        
    
    def helper(self, lists, start, end):
        if start == end:
            return lists[start]
        
        mid = start + (end - start) / 2
        left = self.helper(lists, start, mid)
        right = self.helper(lists, mid + 1, end) # Note here is "mid + 1", not "mid"
        
        return self.mergeTwoLists(left, right)
    
    
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        node = dummy
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                node.next = list1
                node = list1
                list1 = list1.next
            else:
                node.next = list2
                node = list2
                list2 = list2.next
        
        if list1 != None:
            node.next = list1
        else:
            node.next = list2
        
        return dummy.next
        


