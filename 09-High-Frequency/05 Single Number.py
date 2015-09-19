# Single Number
# Given 2*n + 1 numbers, every numbers occurs twice except one, find it.
#
# Example
# Given [1,2,2,1,3,4,3], return 4
#
# Challenge
# One-pass, constant extra space.

"""
    Bitwise exclusive:
    0^0=0, 0^1=1, 1^0=1, 1^1=0
    Add a number twice from 0:
    0 ^0-> 0 ^0 ->0
    0 ^1-> 1 ^1 ->0
    So the number left is the single number we want.
"""

class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        # write your code here
        result = 0
        for i in range(len(A)):
            result = result ^ A[i]
        return result
        
