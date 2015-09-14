# Combination Sum II 
# Given a collection of candidate numbers (C) and a target number 
# (T), find all unique combinations in C where the candidate 
# numbers sums to T.
# Each number in C may only be used once in the combination.
#
# Example
# For example, given candidate set 10,1,6,7,2,1,5 and target 8,
# A solution set is:
# [1,7], [1,2,5], [2,6], [1,1,6]
#
# Note here are two "1"!

class Solution:    
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target): 
        # write your code here
        candidates.sort()
        self.result = []
        self.dfs(candidates, target, 0, [])
        return self.result
    
    def dfs(self, candidates, target, start, path):
        
        if target == 0:
            if path not in self.result: # Note here, avoid duplicates.
                self.result.append(path)
                
        for i in range(start, len(candidates)):
            if candidates[i] > target: 
                return
            self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]])
