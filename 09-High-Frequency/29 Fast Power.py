# Fast Power
# Calculate the (a ^ n) / b where a, b and n are all 32bit integers.
# 
# Example
# For 2^31 % 3 = 2
# Challenge
# O(logn)
#
class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if n == 1:
            return a % b
        if n == 0:
            return 1 % b
            
        product = self.fastPower(a, b, n / 2)
        product = (product * product) % b
        
        if n % 2 == 1:
            product = (product * a) % b
        return product
