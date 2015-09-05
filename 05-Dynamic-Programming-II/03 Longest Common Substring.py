# Longest Common Substring
# Given two strings, find the longest common substring. Return the length of it.
#
# Example
# Given A = "ABCD", B = "CBCE", return 2.
#
# Note
# The characters in substring should occur continuously in original string.
# This is different with subsequence.
#
# Challenge
# O(n x m) time and memory.
#
#

"""This is not Dynamic Programming"""

class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        
        maxLength = 0
        m = len(A)
        n = len(B)
        
        for i in range(m):
            for j in range(n):
                
                length = 0
                while (i + length < m) and (j + length < n) and A[i + length] == B[j + length]:
                    length += 1
                if length > maxLength:
                    maxLength = length
                        
        return maxLength
