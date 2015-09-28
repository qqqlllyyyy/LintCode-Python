# Integer to Roman
# Given an integer, convert it to a roman numeral.
# The number is guaranteed to be within the range from 1 to 3999.
#
# Example
# 4 -> IV, 12 -> XII, 21 -> XXI, 99 -> XCIX
# more examples at: http://literacy.kent.edu/Minigrants/Cinci/romanchart.htm

class Solution:
    # @param {int} n The integer
    # @return {string} Roman representation
    
    # Put a char on the left means to subtract.
    # CM = M-C = 1000-100 = 900, XL = L-X = 50-10 = 40
    
    def intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        list = ''
        for i in range(0, len(values)):
            while num >= values[i]:
                num -= values[i]
                list += numerals[i]
        return list
