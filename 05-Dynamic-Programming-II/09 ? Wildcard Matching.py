# Wildcard Matching
# Implement wildcard pattern matching with support for '?' and '*'.
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
#
# isMatch("aa","a") -> false
# isMatch("aa","aa") -> true
# isMatch("aaa","aa") -> false
# isMatch("aa", "*") -> true
# isMatch("aa", "a*") -> true
# isMatch("ab", "?*") -> true
# isMatch("aab", "c*a*b") -> false


class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: A boolean
    """
    # Note '?' can not match empty sequence!
    def isMatch(self, s, p):
        
        if (s == None and p != None) or (s != None and p == None):
            return False
        
        m, n = len(s), len(p)
        dp = [[False for i in range(n + 1)] for j in range(m + 1)]
        dp[0][0] = True
        
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                if p[j - 1] == '*': # Can add "s[i - 1]=='*'" here, why?
                    if dp[i - 1][j] or dp[i][j - 1]:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                
                elif dp[i - 1][j - 1]:
                    if s[i - 1] == p[j - 1] or s[i - 1] == '?' or p[j - 1]=='?':
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                
                else:
                    dp[i][j] = False
        
        return dp[m][n]
