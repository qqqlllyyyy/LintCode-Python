# Combination Sum
# Given a set of candidate numbers (C) and a target number (T), 
# find all unique combinations in C where the candidate numbers sums to T.
# The same repeated number may be chosen from C unlimited number of times.
#
# For example, given candidate set 2,3,6,7 and target 7, 
# A solution set is: 
# [7] 
# [2, 2, 3]
#
# Note
# All numbers (including target) will be positive integers.
# Elements in a combination must be in non-descending order. 
# The solution set must not contain duplicate combinations.
#

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        self.result = []
        self.dfs(candidates, target, 0, [])
        return self.result
    
    def dfs(self, candidates, target, start, path):
        if target == 0:
            self.result.append(path)
            
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return
            self.dfs(candidates, target - candidates[i], i, path + [candidates[i]])
            # Can not use "path.append(candidates[i])"
            # or path += [candidates[i]] here, why?
    """
    Why this does't work?
    class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # write your code here
        result = []
        if len(candidates) == 0: return result
        candidates.sort()
        path = []
        self.helper(candidates, target, path, 0, result)
        return result
        
    def helper(self, candidates, target, path, index, result):
        if target == 0:
            result.append(path)
            return
        
        prev = -1
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                return
            if prev != -1 and prev == candidates[i]:
                continue # Why this "if" statement here ? 
            path.append(candidates[i])
            self.helper(candidates, target - candidates[i], path, i, result)
            path = path[ : len(path) - 1] * 1
            prev = candidates[i]
    """
            
