# Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without
# repeating characters.
#
# Example
# For example, the longest substring without repeating letters for
# "abcabcbb" is "abc", which the length is 3.
# For "bbbbb" the longest substring is "b", with the length of 1.
#
# Challenge
# O(n) time

"""Similar to 'Longest Substring with At Most K Distinct Characters'"""
class Solution:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        # write your code here
        if s == None or len(s) == 0: return 0
        
        head, tail = 0, 0
        dict = {}
        longest = 0
        
        while head < len(s):
            while head < len(s) and s[head] not in dict:
            # "head" will not move on beacuse it appeared somwhere before.
                dict.setdefault(s[head], 0)
                dict[s[head]] += 1
                head += 1
            
            longest = max(longest, head - tail)
            
            while tail < head:
                del dict[s[tail]]
                tail += 1
                # Since "head" appeared somewhere before. 
                # We can't move on until we deleted the position
                # where "head" first appeared.
                if head < len(s) - 1 and s[tail - 1] == s[head]:

                    break
                
        return longest
