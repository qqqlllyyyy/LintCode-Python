# Maximum Subarray II
# Given an array of integers, find two non-overlapping subarrays
# which have the largest sum.
# The number in each subarray should be contiguous. Return the largest sum.
#
# Example
# For given [1, 3, -1, 2, -1, 2], the two subarrays are [1, 3]
# and [2, -1, 2] or [1, 3, -1, 2] and [2], they both have the largest sum 7.
#
# Note
# The subarray should contain at least one number
# Challenge
# Can you do it in time complexity O(n)?
#
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """

    # My method. Similar to the problem "Maximum Subarray"
    
    def maxTwoSubArrays(self, nums):
        # write your code here 
        result = float("-infinity")
        for i in range(0, len(nums) - 1):
            new = self.maxSubArray(nums[:i+1]) + self.maxSubArray(nums[i+1:])
            result = max(result, new)
        return result
        
    def maxSubArray(self, nums):
        result = float("-infinity")
        sum, minSum = 0, 0
        for i in range(len(nums)):
            sum += nums[i]
            result = max(result, sum - minSum)
            minSum = min(minSum, sum)
        return result


    # O(n) method !!
    
    def maxTwoSubArrays(self, nums):
        # write your code here   
        # write your code here   
        n = len(nums)
        a = nums[:]
    	aa = nums[:]
        for i in range(1, n):
            a[i] = max(nums[i], a[i-1] + nums[i])
            # a[i] means maximum value of a subarray ending with nums[i].
            aa[i] = max(a[i], aa[i-1])
            # aa[i] means maximum value of a subarray with an end index
            # less than or equal to i.
        b = nums[:]
    	bb = nums[:]
        for i in range(n-2, -1, -1):
            b[i] = max(b[i+1] + nums[i], nums[i])
            bb[i] = max(b[i], bb[i+1])
        mx = -65535
        for i in range(n - 1):
            mx = max(aa[i]+b[i+1], mx)

        return mx

