# Longest Words
# Given a dictionary, find all of the longest words in the dictionary.
#
# Example
# Given:
# [
#  "dog",
#  "google",
#  "facebook",
#  "internationalization",
#  "blabla"
# ]
# the longest words are(is) ["internationalization"].
#
# Challenge
# It's easy to solve it in two passes, can you do it in one pass?

class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        # write your code here
        
        result = []
        length = 0
        
        for i in range(len(dictionary)):
            if len(dictionary[i]) > length:
                length = len(dictionary[i])
                result = [dictionary[i]]
            
            elif len(dictionary[i]) == length:
                result.append(dictionary[i])
        
        return result
