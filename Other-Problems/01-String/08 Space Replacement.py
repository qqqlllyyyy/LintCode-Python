# Space Replacement
# Write a method to replace all spaces in a string with %20.
# The string is given in a characters array, you can assume it has
# enough space for replacement and you are given the true length of
# the string.
#
# Example
# Given "Mr John Smith", length = 13.
# The string after replacement should be "Mr%20John%20Smith".
#
# If you are using Java or Python, please use characters array
# instead of string.
#
# Challenge
# Do it in-place.

class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here
        if string == None: return None
        
        result = []
        numberZero = 0
        for i in range(len(string)):
            if string[i] == ' ':
                result.append('%')
                result.append('2')
                result.append('0')
                numberZero += 1
            else:
                result.append(string[i] )
 
        newLength = length + 2 * numberZero
        for i in range(newLength):
            string[i] = result[i]
        
        return
