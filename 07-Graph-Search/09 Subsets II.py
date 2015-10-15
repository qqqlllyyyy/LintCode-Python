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
        self.dfs([], 0, S)
        return self.result
        
        
    def dfs(self, path, start, S):
        #if path not in self.result:
        self.result.append(path)
        
        for i in range(start, len(S)):
            if i != start and S[i] == S[i - 1]: # Understand this!
                continue
            else:
                self.dfs(path + [S[i]], i + 1, S)
        
