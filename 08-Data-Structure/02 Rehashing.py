# Rehashing
# The size of the hash table is not determinate at the very 
# beginning. If the total size of keys is too large (e.g. size >= 
# capacity / 10), we should double the size of the hash table and 
# rehash every keys. Say you have a hash table looks like below:
#
# Example
# Given [null, 21->9->null, 14->null, null],
# return [null, 9->null, null, null, null, 21->null, 14->null, null]
#
# For more info: http://www.lintcode.com/en/problem/rehashing/#
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
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        if len(hashTable) <= 0:
            return hashTable
        
        n = 2 * len(hashTable)
        newTable = [None for i in range(n)]
        for i in range(len(hashTable)):
            while hashTable[i] != None:
                
                newIndex = hashTable[i].val % n
                if newTable[newIndex] == None:
                    newTable[newIndex] = ListNode(hashTable[i].val)
                else:
                    dummy = newTable[newIndex]
                    while dummy.next != None:
                        dummy = dummy.next
                    dummy.next = ListNode(hashTable[i].val)
                
                hashTable[i] = hashTable[i].next
                
        return newTable
        # Take care about each element in "newTable", they are nodes.
        # Understand the steps.

