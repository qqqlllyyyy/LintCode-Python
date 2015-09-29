# Longest Substring with At Most K Distinct Characters
# Given a string s, find the length of the longest substring T that
# contains at most k distinct characters.
#
# Example
# For example, Given s = "eceba", k = 3,
# T is "eceb" which its length is 4.
#
# Challenge
# O(n), n is the size of the string s.

class Solution:
    # @param s : A string
    # @return : An integer
    """
        Try to understand
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k == 0:
            return 0
            
        hash = {}
        head, tail = 0, 0
        longest = 0
        while head < len(s):
            while head < len(s) and (s[head] in hash or len(hash) < k):
                hash.setdefault(s[head], 0)
                hash[s[head]] += 1
                head += 1
            longest = max(longest, head - tail)
            while tail < head and len(hash) == k:
                # Move tail forward so that it reach the first position
                # where len(hash) != k
                hash[s[tail]] -= 1
                if hash[s[tail]] == 0:
                    del hash[s[tail]]
                tail += 1
        return longest
