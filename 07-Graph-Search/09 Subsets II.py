# Subsets II
# Given a list of numbers that may has duplicate numbers, return all 
# possible subsets
#
# Example
# If S = [1,2,2], a solution is:
# [
#  [2],
#  [1],
#  [1,2,2],
#  [2,2],
#  [1,2],
#  []
# ]
# Note
# Each element in a subset must be in non-descending order.
# The ordering between two subsets is free.
# The solution set must not contain duplicate subsets.
class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        # write your code here
        self.result = []
        if S == None or len(S) == 0:
            return self.result
        S.sort()
        visited = [0 for i in range(len(S))]
        self.dfs([], 0, visited, S)
        return self.result
    
    def dfs(self, path, start, visited, S):
        if path not in self.result:
            self.result.append(path)
        for i in range(start, len(S)):
            if visited[i] == 0:
                visited[i] = 1
                self.dfs(path + [S[i]], i + 1, visited, S)
                visited[i] = 0
        
