# Roman to Integer
# Given a roman numeral, convert it to an integer.
# The answer is guaranteed to be within the range from 1 to 3999.
#
# Example
# IV -> 4, XII -> 12, XXI -> 21, XCIX -> 99

"""Similar to 'Integer to Roman'"""
class Solution:
    # @param {string} s Roman representation
    # @return {int} an integer
    def romanToInt(self, s):
        # Write your code here
        result = 0
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        i = 0
        while i < len(s):
            
            for j in range(len(values)):
                # Check for two characters first
                if s[i: i + 2] == numerals[j]:
                    result += values[j]
                    i += 2
                    break
                
                elif s[i] == numerals[j]:
                    result += values[j]
                    i += 1
                    break
                
            
        return result
                
