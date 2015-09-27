# Add Binary
# Given two binary strings, return their sum (also a binary string).
#
# Example
# a = 11
# b = 1
# Return 100

class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        # Write your code here
        aIndex = len(a) - 1
        bIndex = len(b) - 1
        flag = 0
        result = ''
        
        while aIndex >= 0 and bIndex >= 0:
            # Can not remove the "ing()" below.
            num = int(a[aIndex]) + int(b[bIndex]) + flag
            flag = num / 2
            num = num % 2
            # Can not remove "str()".
            result = str(num) + result
            aIndex -= 1
            bIndex -= 1
            
        while aIndex >= 0:
            num = int(a[aIndex]) + flag
            flag = num / 2
            num = num % 2
            result = str(num) + result
            aIndex -= 1
        
        while bIndex >= 0:
            num = int(b[bIndex]) + flag
            flag = num / 2
            num = num % 2
            result = str(num) + result
            bIndex -= 1
        
        if flag == 1: # Here flag is an int. Can not use " flag == '1' "!
            result = '1' + result
            
        return result
        
    
