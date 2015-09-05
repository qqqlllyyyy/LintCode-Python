# Distinct Subsequences
# Given a string S and a string T, count the number of distinct 
# subsequences of T in S.
# A subsequence of a string is a new string which is formed from 
# the original string by deleting some (can be none) of the 
# characters without disturbing the relative positions of the 
# remaining characters. (ie, "ACE" is a subsequence of "ABCDE"
# while "AEC" is not).
#
# Example
# Given S = "rabbbit", T = "rabbit", return 3.
#
# Challenge
# Do it in O(n2) time and O(n) memory.
# O(n2) memory is also acceptable if you do not know how to optimize memory.
#


class Solution: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        
        m = len(S)
        n = len(T)
        
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j]
                if S[i - 1] == T[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        
        return dp[m][n]
