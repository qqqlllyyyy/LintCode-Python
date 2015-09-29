# Binary Representation
# Given a (decimal - e.g. 3.72) number that is passed in as a string,
# return the binary representation that is passed in as a string. If the
# fractional part of the number can not be represented accurately in binary
# with at most 32 characters, return ERROR.
#
# Example
# For n = "3.72", return "ERROR".
# For n = "3.5", return "11.1".

class Solution:
    #@param n: Given a decimal number that is passed in as a string
    #@return: A string
    
    """ Remember here n is a string """
    
    def binaryRepresentation(self, n):
        # write you code here
        if '.' not in n:
            return self.parseInteger(n)
        params = n.split('.')
        
        flt = self.parseFloat(params[1])
        if flt == 'ERROR':
            return flt
        if flt == '0' or flt == '':
            return self.parseInteger(params[0])
        
        return self.parseInteger(params[0]) + '.' + flt
        
        
    def parseInteger(self, string):
        if string == '0' or string == '': return '0'
        n = int(string)
        binary = ''
        # Remeber the way to change an integer to binary representation.
        while n != 0:
            binary = str(n % 2) + binary
            n /= 2
        return binary
    
    
    def parseFloat(self, str):
        d = float('0.' + str)
        binary = ''
        #set = []
        while d > 0:
            # If we remove "or d in set", the code can also pass the test.
            # So it seems that we don't need the 'set'.
            if len(binary) > 32 or d in set:
                return "ERROR"
            #set.append(d)
            
            #Rember the way to change a float number to binary representation
            d = d * 2
            if d >= 1:
                binary += '1'
                d -= 1
            else:
                binary += '0'
        return binary
        
        
        
        
        
