# Two Strings Are Anagrams
# Write a method anagram(s,t) to decide if two strings are anagrams or not.
#
# Example
# Given s="abcd", t="dcab", return true.
# Challenge
# O(n) time, O(1) extra space
#

class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        if len(s) != len(t): return False
        dict = {}
        for i in range(256): # May contain spaces
            dict[chr(i)] = 0
        
        for i in range(len(s)):
            dict[s[i]] += 1
        for i in range(len(t)):
            dict[t[i]] -= 1
            if dict[t[i]] < 0:
                return False
        return True
