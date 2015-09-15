# Word Ladder
# Given two words (start and end), and a dictionary, find the length 
# of shortest transformation sequence from start to end, such that:
# 1. Only one letter can be changed at a time
# 2. Each intermediate word must exist in the dictionary
#
# Example
# Given:
# start = "hit", end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
# Note
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
#
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        # write your code here
        if dict == None or len(dict) == 0:
            return 0
        A = [start] # A contains the nodes we have visited at least once.
        B = [start]
        length = 1
        while len(B) > 0:
            length = length + 1
            for i in range(len(B)):
                word = B.pop(0)
                print word
                print self.getNextWords(word, dict)
                for nextWord in self.getNextWords(word, dict):
                    if nextWord not in A:
                        if nextWord == end:
                            return length
                    A.append(nextWord)
                    B.append(nextWord)
        return 0 # Don't forget this
        
    # replace character of a string at given index to a given character
    # return a new string
    
    def replace(self, S, index, c):
        return S[: index] + c + S[index + 1:]
    
    # get connections with given word.
    # for example, given word = 'hot', dict = {'hot', 'hit', 'hog'}
    # it will return ['hit', 'hog']
    
    def getNextWords(self, word, dict):
        nextWords = []
        for i in 'abcdefghijklmnopqrstuvwxyz':
            for j in range(len(word)):
                if i != word[j]:
                    newWord = self.replace(word, j, i)
                    if newWord in dict:
                        nextWords.append(newWord)
        return nextWords
