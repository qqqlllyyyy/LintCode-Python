# Single Number III
# Given 2*n + 2 numbers, every numbers occurs twice except two, find them.
#
# Example
# Given [1,2,2,3,4,4,5,3] return 1 and 5
#
# Challenge
# O(n) time, O(1) extra space.
#
#
class Solution:
    """
    @param A : An integer array
    @return : Two integer
    """
    def singleNumberIII(self, A):
        # write your code here
        xor = 0
        for i in range(len(A)):
            xor ^= A[i]
        
        # lastBit is the last bit to be '1'.
        # target1 ^ target2 = 1 means they are different on this bit.
        # We can thus divide the numbers into two groups
        lastBit = xor - (xor & (xor - 1))
        # Can not be "xor - xor & (xor - 1)".
        # We do need the parentheses !!
        
        group0, group1 = 0, 0
        for i in range(len(A)):
            if (A[i] & lastBit) == 0:
                group0 ^= A[i]
            else:
                group1 ^= A[i]
                
        return group0, group1
            
