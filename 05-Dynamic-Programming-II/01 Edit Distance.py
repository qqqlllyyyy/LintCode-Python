# Edit Distance
# Given two words word1 and word2, find the minimum number of 
# steps required to convert word1 to word2. (each operation is 
# counted as 1 step.)
# You have the following 3 operations permitted on a word:
# 1. Insert a character
# 2. Delete a character
# 3. Replace a character
#
# Example
# Given word1 = "mart" and word2 = "karma", return 3.
#
#



class Solution: 
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        
        m = len(word1)
        n = len(word2)
        
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(n + 1):
            dp[0][i] = i
        for i in range(m + 1):
            dp[i][0] = i
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
        
        return dp[m][n]
