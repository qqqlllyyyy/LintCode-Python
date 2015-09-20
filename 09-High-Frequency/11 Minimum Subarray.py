# Minimum Subarray
# Given an array of integers, find the subarray with smallest sum.
# Return the sum of the subarray.
#
# Example 
# For [1, -1, -2, 1], return -3
#
# Note
# The subarray should contain at least one integer.
#
class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        if nums == None or len(nums) == 0: return 0
        
        # Take inverse, then it's the same question as "Maximum Subarray"
        reverse = []
        for i in range(len(nums)):
            reverse.append(-nums[i])
        
        result = float("-infinity")
        sum, minSum = 0, 0 # Record the minimum sum so far.
        
        for i in range(len(reverse)):
            sum += reverse[i]
            result = max(result, sum - minSum)
            minSum = min(minSum, sum)
            
        return -result
            

