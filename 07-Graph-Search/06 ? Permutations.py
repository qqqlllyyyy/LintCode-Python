# Permutations
# Given a list of numbers, return all possible permutations.
#
# Example
# For nums = [1,2,3], the permutations are:
# [
#  [1,2,3],
#  [1,3,2],
#  [2,1,3],
#  [2,3,1],
#  [3,1,2],
#  [3,2,1]
# ]
#
# Challenge
# Do it without recursion.
#
class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    # Recursion
    def permute(self, nums):
        # write your code here
        self.result = []
        if nums == None or len(nums) == 0: 
            return self.result
        self.dfs([], nums)
        return self.result
    
    def dfs(self, path, nums):
        if len(path) == len(nums):
            self.result.append(path)
            return 
        for i in range(len(nums)):
            if nums[i] not in path:
                self.dfs(path + [nums[i]], nums)
    
    # Non-recursion. Why?       
    def permute(self, nums):
        if nums is None:
            return []
        nums = sorted(nums)
        permutation = []
        stack = [-1]
        permutations = []
        while len(stack):
            index = stack.pop()
            index += 1
            while index < len(nums):
                if nums[index] not in permutation:
                    break
                index += 1
            else:
                if len(permutation):
                    permutation.pop()
                continue

            stack.append(index)
            stack.append(-1)
            permutation.append(nums[index])
            if len(permutation) == len(nums):
                permutations.append(list(permutation))
        return permutations
                

