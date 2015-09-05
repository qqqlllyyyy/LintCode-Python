# Longest Common Subsequence
# Given two strings, find the longest common subsequence (LCS).
# Your code should return the length of LCS.
#
# Example
# For "ABCD" and "EDCA", the LCS is "A" (or "D", "C"), return 1.
# For "ABCD" and "EACB", the LCS is "AC", return 2.
#

"""Clarification:
A substring of a string S is another string S' that occurs "in" S.
For example, "the best of" is a substring of "It was the best of times".
This is not to be confused with subsequence, which is a generalization of
substring. For example, "Itwastimes" is a subsequence of "It was the best of
times", but not a substring.
"""

class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        
        m = len(A)
        n = len(B)
        
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]
