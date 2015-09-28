# Reverse Words in a String
# Given an input string, reverse the string word by word.
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#
# Clarification
# 1. What constitutes a word?
#    A sequence of non-space characters constitutes a word.
# 2. Could the input string contain leading or trailing spaces?
#    Yes. However, your reversed string should not contain leading
#    or trailing spaces.
# 3. How about multiple spaces between two words?
#    Reduce them to a single space in the reversed string.
#

class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        # write your code here
        if s == '': return s
        resultList = []
        
        start, end = -1, 0
        
        for i in range(len(s) - 1):
            
            if s[i] == ' ' and s[i + 1] != ' ':
                start = i
                
            if s[i] != ' ' and s[i + 1] == ' ':
                end = i
                resultList.append(s[start + 1 : end + 1])
            
            if s[i + 1] != ' ' and i == len(s) - 2:
                resultList.append(s[start + 1 : ])
        
        j = len(resultList) - 1
        result = ''
        while j >= 0:
            result += resultList[j]
            result += ' '
            j -= 1
        return result[ : len(result) - 1]
            
