# Subsets
# Given a set of distinct integers, return all possible subsets.
#
# Example
# If S = [1,2,3], a solution is:
# [
#  [3],
#  [1],
#  [2],
#  [1,2,3],
#  [1,3],
#  [2,3],
#  [1,2],
#  []
# [
#
# Note
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.

class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        self.result = []
        if S == None or len(S) == 0:
            return self.result
        S.sort() # Don't forget to sort it.
        self.dfs([], 0, S)
        return self.result
    
    def dfs(self, path, start, S):
        self.result.append(path)
        for i in range(start, len(S)):# Can not start from "start+1" here
            # Beause you will miss S[0].
            self.dfs(path + [S[i]], i + 1, S)
