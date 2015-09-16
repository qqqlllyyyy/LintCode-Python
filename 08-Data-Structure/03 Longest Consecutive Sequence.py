# Longest Consecutive Sequence
# Given an unsorted array of integers, find the length of the longest 
# consecutive elements sequence.
#
# Example
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4].
# Return its length: 4.
#
# Clarification
# Your algorithm should run in O(n) complexity.
#

class Solution:
    """
    @param num, a list of integer
    @return an integer
    """
    # Good method, read again.
    def longestConsecutive(self, num):
        # write your code here
        dict = {}
        for i in num:
            dict[i] = 0
        
        result = 1
        for i in num:
            if dict[i] != 1: # 0 means it has not been visited.
                current_max = 1
                tmp = i
                while tmp + 1 in dict:
                    current_max += 1
                    tmp += 1
                    dict[tmp] = 1
                tmp = i
                while tmp - 1 in dict:
                    current_max += 1
                    tmp -= 1
                    dict[tmp] = 1
                
                result = max(result, current_max)
        return result
    
    # My method, not O(n)
    def longestConsecutive(self, num):
        if len(num) <= 1:
            return len(num)
        num.sort()
        result = 1
        tmp = 1
        for i in range(len(num) - 1):
            if num[i + 1] == num[i] + 1:
                tmp += 1
                result = max(result, tmp)
            elif num[i + 1] == num[i]:
                continue
            else:
                tmp = 1
        return result
        
                
            
        
