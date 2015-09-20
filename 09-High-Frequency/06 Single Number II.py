# Single Number II
# Given 3*n + 1 numbers, every numbers occurs triple times except one, find it.
#
# Example
# Given [1,1,2,3,3,3,2,2,4,1] return 4
#
# Challenge
# One-pass, constant extra space.
#
#
class Solution:
    """
	@param A : An integer array
	@return : An integer
    """
    def singleNumberII(self, A):
        # write your code here
        if A == None or len(A) == 0: return -1

        # Get a list of all powers of 3.
        # 20 should be enough for any number less than 2^32
        power3 = [1 for i in range(20)]
        for i in range(1, 20):
            power3[i] = 3 * power3[i - 1]
        
        # Convert any in A into ternary mode            
        bit = [0 for i in range(20)]
        for i in range(20):
            for j in range(len(A)):
                bit[i] = bit[i] + ((A[j] / power3[i]) % 3)
        
        # The number left is what we want
        result = 0
        for i in range(20):
            result += (bit[i] % 3) * power3[i]
        
        return result
                
            
        
