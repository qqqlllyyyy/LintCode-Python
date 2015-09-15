# Word Ladder II
# Given two words (start and end), and a dictionary, find all shortest 
# transformation sequence(s) from start to end, such that:
# 1. Only one letter can be changed at a time
# 2. Each intermediate word must exist in the dictionary
#
# Example
# Given:
# start = "hit", end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# Return
# [
#  ["hit","hot","dot","dog","cog"],
#  ["hit","hot","lot","log","cog"]
# ]
#
# Note
# All words have the same length.
# All words contain only lowercase alphabetic characters.
#
"""
    Why can't it pass?
"""
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        ladders = []
        map = {}
        distance = {}
        self.bfs(map, distance, start, end, dict)
        
        path = []
        
        self.dfs(ladders, path, end, start, distance, map)
        return ladders
    
    def bfs(self, map, distance, start, end, dict):
        q = [start]
        distance[start] = 0
        for s in dict:
            map[s] = []
        
        while len(q) > 0:
            curr = q.pop(0)
            nextList = self.expand(curr, dict)
            for node in nextList:
                map[node] += curr
                if node not in distance:
                    distance[node] = distance[curr] + 1
                    q.append(node)
    
    def expand(self, curr, dict):
        nextWordList = []
        for i in range(len(curr)):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                if j != curr[i]:
                    nextWord = curr[ : i] + j + curr[i + 1 : ]
                    if nextWord in dict:
                        nextWordList.append(nextWord)
        return nextWordList
    
    def dfs(self, ladders, path, crt, start, distance, map):
        newpath = path + [crt]
        if crt == start:
            newpath.reverse()
            ladders.append(newpath)
            newpath.reverse()
        else:
            for next in map[crt]:
                if next in distance and distance[next] == distance[crt] + 1:
                    self.dfs(ladders, path + [crt], next, start, distance, map)
        
        
        
