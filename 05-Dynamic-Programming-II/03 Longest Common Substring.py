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

    # Dynamic Programming
    
    def longestCommonSubstring(self, A, B):
        
        m = len(A)
        n = len(B)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
        
        maxLength = 0
        for i in range(m + 1):
            for j in range(n + 1):
                maxLength = max(maxLength, dp[i][j])
        
        return maxLength

    # Bad Method
    
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
