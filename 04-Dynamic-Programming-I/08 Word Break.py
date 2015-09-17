# Word Break
# Given a string s and a dictionary of words dict, determine if s can 
# be break into a space-separated sequence of one or more 
# dictionary words.
#
# Example
# Given s = "lintcode", dict = ["lint", "code"].
# Return true because "lintcode" can be break as "lint code".
#

class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        
        n = len(s)
        dp = [False for i in range(n + 1)]
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(0, i):
                if dp[j] and s[j:i] in dict:
                    dp[i] = True
        return dp[n]
        
        
        
        
        
