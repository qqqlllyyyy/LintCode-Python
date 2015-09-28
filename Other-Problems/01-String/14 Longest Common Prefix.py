# Longest Common Prefix
# Given k strings, find the longest common prefix (LCP).
#
# Example
# For strings "ABCD", "ABEF" and "ACEF", the LCP is "A"
# For strings "ABCDEFG", "ABCEFG" and "ABCEFA", the LCP is "ABC"

class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        if strs == None or len(strs) == 0:
            return ""
        
        result = strs[0]
        for i in range(1, len(strs)):
            j = 0
            # Be careful about the conditions.
            while j < len(strs[i]) and j < len(result) and result[j] == strs[i][j]:
                j += 1
                
            result = result[: j]
        return result
