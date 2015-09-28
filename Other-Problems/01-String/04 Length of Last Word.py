# Length of Last Word
# Given a string s consists of upper/lower-case alphabets and empty
# space characters ' ', return the length of last word in the string.
# If the last word does not exist, return 0.
#
# Example
# Given s = "Hello World", return 5.
#
# Note
# A word is defined as a character sequence consists of non-space
# characters only.

class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        # Write your code here
        if s == '': return 0
        preWord = -1
        endWord = 0 # It's ok to let "endWord = len(s) - 1" here
        for i in range(len(s) - 1):
            if s[i] == ' ' and s[i + 1] != ' ':
                preWord = i
            if s[i] != ' ' and s[i + 1] == ' ':
                endWord = i
            if s[i + 1] != ' ' and i + 1 == len(s) - 1:
                endWord = i + 1
                
        return endWord - preWord

    """
    Need to use two pointers, since we need to remember the start index
    and the end index. The string may end with space: 'a b '
    """
