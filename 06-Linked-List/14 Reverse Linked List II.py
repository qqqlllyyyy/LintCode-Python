"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        
        if m >= n or head == None:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        # Locath mth node.
        for i in range(1, m):
            if head == None:
                return None
            head = head.next
        
        # Mark (m-1)th node and mth node
        # Then have two pointer move from m to n: "nNode" and "postnNode"
        premNode = head
        mNode = head.next
        nNode = mNode
        postnNode = mNode.next
        for i in range(m, n):
            if postnNode == None:
                return None
            temp = postnNode.next
            postnNode.next = nNode
            nNode = postnNode
            postnNode = temp
        premNode.next = nNode
        mNode.next = postnNode
        
        return dummy.next
