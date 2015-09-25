# Trailing Zeros
# Write an algorithm which computes the number of trailing
# zeros in n factorial.
#
# Example
# 11! = 39916800, so the out should be 2
#
# Challenge
# O(log N) time
#
#

class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        sum = 0
        
        # It will be determined by how many 5's there are.
        
        while n != 0:
            sum += n / 5
            n = n / 5
        return sum
            
