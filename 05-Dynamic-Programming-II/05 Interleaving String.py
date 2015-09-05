# Interleaving String
# Given three strings: s1, s2, s3, determine whether s3 is formed by 
# the interleaving of s1 and s2.
#
# Example
# For s1 = "aabcc", s2 = "dbbca"
# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.
#
# Challenge
# O(n2) time or better

class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        
        if len(s1) + len(s2) != len(s3):
            return False
            
        m = len(s1)
        n = len(s2)
        
        dp = [[False for i in range(n + 1)] for j in range(m + 1)]
        dp[0][0] = True
        
        for i in range(1, m + 1):
            if dp[i - 1][0] and s1[i - 1] == s3[i - 1]:
                dp[i][0] = True
        for j in range(1, n + 1):
            if dp[0][j - 1] and s2[j - 1] == s3[j - 1]:
                dp[0][j] = True
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]):
                    dp[i][j] = True
                    
        return dp[m][n]
