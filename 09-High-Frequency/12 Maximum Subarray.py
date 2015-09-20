# Maximum Subarray
# Given an array of integers, find a contiguous subarray which has 
# the largest sum.
#
# Example
# Given the array [-2,2,-3,4,-1,2,1,-5,3], the contiguous 
# subarray [4,-1,2,1] has the largest sum = 6
#
# Challenge
# Can you do it in time complexity O(n)?
#
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if nums == None or len(nums) == 0: return 0
        
        result = float("-infinity")
        sum, minSum = 0, 0
        for i in range(len(nums)):
            sum += nums[i]
            
            # For the following two steps, we can not change the order!
            # Because if we update "minSum" first, the result may be 0,
            # which is sum minus itself. (nums = [-1])
            result = max(result, sum - minSum)
            minSum = min(sum, minSum)
            
        return result
