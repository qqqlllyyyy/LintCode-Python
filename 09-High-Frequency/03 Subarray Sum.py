# Subarray Sum
# Given an integer array, find a subarray where the sum of numbers 
# is zero. Your code should return the index of the first number and 
# the index of the last number.
#
# Example
# Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].
# Note
# There is at least one subarray that it's sum equals to zero.

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    # Ordinary method with high time complexity, skip it.
    def subarraySum(self, nums):
        # write your code here
        for i in range(len(nums)):
            for j in range(len(nums)):
                sum = 0
                for k in range(i, j + 1):
                    sum += nums[k]
                if sum == 0:
                    return i, j
                    
    # Better way. If the sum of first i elements is equivalent to the 
    # sum of firs j elements. Then the sum from (i+1)th value to jth 
    # value is zero.
    def subarraySum(self, nums):
        dict = {0: -1} # Initialization
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum in dict:
                return dict[sum] + 1, i 
                # Pay attention to the values here.
            dict[sum] = i
