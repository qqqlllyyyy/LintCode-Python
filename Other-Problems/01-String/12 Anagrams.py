# Anagrams
# Given an array of strings, return all groups of strings that are anagrams.
#
# Example
# Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].
# Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].
#
# All inputs will be in lower-case

class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # O(n), O(n)
        
        d = {}
        for str in strs:
            # 'join' is a function like 'implode' in PHP
            sorted_str = ''.join(sorted(str))
            # sorted() is a built-in function in Python:
            # test = 'BABC', sorted(test) = ['A', 'B', 'B', 'C']
            
            if sorted_str not in d:
                d[sorted_str] = [str]
            else:
                d[sorted_str] += [str]
            
        result = []
        for str in d:
            if len(d[str]) >= 2:
                result += d[str]
        return result
