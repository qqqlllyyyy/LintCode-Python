# Unique Characters
# Implement an algorithm to determine if a string has all unique characters.
#
# Example
# Given "abc", return true.
# Given "aab", return false.
# Challenge
# What if you can not use additional data structures?
#
class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        # write your code here
        dict = {}
        for i in range(256):
            dict[chr(i)] = 0
        for i in range(len(str)):
            dict[str[i]] += 1
            if dict[str[i]] > 1:
                return False
        return True

    """How to do it without additional data structures?"""
