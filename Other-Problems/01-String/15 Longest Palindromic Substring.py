# Longest Palindromic Substring
# Given a string S, find the longest palindromic substring in S. You may
# assume that the maximum length of S is 1000, and there exists one unique
# longest palindromic substring.
#
# Example
# Given the string = "abcdzdcab", return "cdzdc".
#
# Challenge
# O(n^2) time is acceptable. Can you do it in O(n) time.
#

class Solution:
    # @param {string} s input string
    # @return {string} the longest palindromic substring
    def getlongestpalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1 : r]
        
    def longestPalindrome(self, s):
        palindrome = ''
        for i in range(len(s)):
            # Number of chars may be odd or even
            len1 = len(self.getlongestpalindrome(s, i, i))
            if len1 > len(palindrome): palindrome = self.getlongestpalindrome(s, i, i)
            len2 = len(self.getlongestpalindrome(s, i, i + 1))
            if len2 > len(palindrome): palindrome = self.getlongestpalindrome(s, i, i + 1)
        return palindrome
        
# O(n) method: http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
