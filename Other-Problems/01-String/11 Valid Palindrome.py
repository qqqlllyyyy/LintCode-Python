# Valid Palindrome
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
# Example
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
# For the purpose of this problem, we define empty string as valid palindrome.
#
# Challenge
# O(n) time without extra memory.
#
class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        # Write your code here
        if s == None or len(s) == 0: return True

        start, end = 0, len(s) - 1
        while start < end:
            while start < len(s) and not self.isValid(s[start]):
                start += 1
            if start == len(s): # For empty string '.,,. ,'
                return True
            
            while end >= 0 and not self.isValid(s[end]):
                end -= 1
            
            if s[start].upper() != s[end].upper():
                return False
            else:
                start += 1
                end -= 1
                
        return True
    
    def isValid(self, k):
        if 65 <= ord(k) <= 90 or 97 <= ord(k) <= 122 or 48 <= ord(k) <= 57:
            # a-z, A-Z, 0-9
            return True
        return False
        
