# Count and Say
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
#
# Example
# Given n = 5, return "111221".
#
# The sequence of integers will be represented as a string.


class Solution:
    # @param {int} n the nth
    # @return {string} the nth sequence
    def countAndSay(self, n):
        # Write your code here
        
        oldString = '1'
        for i in range(1, n):
            result = '';
            j = 0
            while j < len(oldString):
                count = 1
                while j + 1 < len(oldString) and oldString[j] == oldString[j + 1]:
                    count += 1
                    j += 1
                result += str(count)
                result += oldString[j]
                j += 1 # Don't forget this part.
            
            oldString = result
        
        return oldString
            
