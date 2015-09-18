# Copy List with Random Pointer Show result 
# A linked list is given such that each node contains an additional 
# random pointer which could point to any node in the list or null.
# Return a deep copy of the list.
#
# Challenge
# Could you solve it with O(1) space?
#
#

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if head == None: return None
        
        dict1 = {None: None} # We need to let "dict1[None]=None" because 
        # for a particular 'node', node.random may be None
        # The we will encounter an error by running 'dict1[node.randow]'.
        
        prehead = RandomListNode(0)
        prehead.next = head
        
        dummy = RandomListNode(0)
        pre = dummy
        
        # Loop all nodes and copy ".next"
        while head != None:
            newNode = RandomListNode(head.label)
            pre.next = newNode
            pre = newNode
            dict1[head] = newNode
            head = head.next
            
        # Loop again and copy ".random"    
        head = prehead.next
        pre = dummy.next
        while head != None:
            head_random = dict1[head.random]
            pre.random = head_random
            pre = pre.next
            head = head.next
        
        return dummy.next
            
