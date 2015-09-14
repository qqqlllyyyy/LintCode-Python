# Permutations II
# Given a list of numbers with duplicate number in it. Find all
# unique permutations.
#
# Example
# For numbers [1,2,2] the unique permutations are:
# [
#  [1,2,2],
#  [2,1,2],
#  [2,2,1]
# ]
#
# Challenge
# Do it without recursion.
#
class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        self.result = []
        if nums == None or len(nums) == 0:
            return self.result
        nums.sort()
        visited = [0 for i in range(len(nums))]
        self.dfs([], visited, nums)
        return self.result
    
    def dfs(self, path, visited, nums):
        if len(path) == len(nums):
            if path not in self.result:
                self.result.append(path)
                
        for i in range(len(nums)):
            # Pay attention to this part. There may be duplicates, so
            # we cannot use "if nums[i] in path", there may be 
            # nums[i] = nums[j]
            if visited[i] == 0:
                visited[i] = 1
                self.dfs(path + [nums[i]], visited, nums)
                visited[i] = 0
    
    # How to do this withour recursion?
            

