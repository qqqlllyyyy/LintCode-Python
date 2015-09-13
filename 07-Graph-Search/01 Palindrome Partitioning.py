# Palindrome Partitioning
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.
#
# Example
# given s = "aab", Return:
# [
#  ["aa","b"],
#  ["a","a","b"]
# ]

class Solution:
    # @param s, a string
    # @return a list of lists of string
    
    def partition(self, s):
        self.string = s
        self.result = [] # Try not use "self." later
        self.length = len(s)
        self.isPalindrome = []
        
        # Remeber this method to make a table "isPalindrome"! 
        # Same as the problem "Palindrome Partitioning II" in DP section.
        for start in range(0, len(s)):
            self.isPalindrome.append([])
            
        for length in range(0,len(s)):
            for start in range(0, len(s)-length):
                if length == 0:
                    self.isPalindrome[start].append(True)
                elif length == 1:
                    self.isPalindrome[start].append(s[start]==s[start+1])
                else:
                    self.isPalindrome[start].append(self.isPalindrome[start+1][length-2] and s[start]==s[start+length])
                    
        self.dfs(0, [])
        return self.result
        
        
    def dfs(self, start, L):
        if start == self.length:
            self.result.append(L)
            return
        for end in range(start, self.length):
            if self.isPalindrome[start][end - start] == True:
                self.dfs(end + 1, L[:] + [self.string[start: end + 1]])
            # make a copy of list L and add a substring
        
        
    
