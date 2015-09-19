# O(1) Check Power of 2
# Using O(1) time to check whether an integer n is a power of 2
#
# Example
# For n=4, return true;
#
# Challenge
# O(1) time
#
# Bitwise source: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_Operators

class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, num):
        # write your code here
        return num != 0 and ((num & (num - 1)) == 0)
