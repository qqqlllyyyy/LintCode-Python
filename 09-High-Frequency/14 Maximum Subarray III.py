# Maximum Subarray III
# Given an array of integers and a number k, find k
# non-overlapping subarrays which have the largest sum.
# The number in each subarray should be contiguous.
# Return the largest sum.
#
# Example
# Given [-1,4,-2,3,-2,3], k=2, return 8
# Note
# The subarray should contain at least one number

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """

    """
    f[i][j] means the largest result when we split first j numbers
    into i parts. nums[j] should be included in the last subarray.
    """
    def maxSubArray(self, nums, k):
        
        f = [[0 for i in range(len(nums))] for j in range(k + 1)]
        
        for i in range(1, k + 1):
            sum = 0
            for j in range(i):
                sum += nums[j]
            f[i][i - 1] = sum
            
        for i in range(1, len(nums)):
            f[1][i] = max(f[1][i - 1] + nums[i], nums[i])
        
        for i in range(2, k + 1):
            for n in range(i, len(nums)):
                curMax = f[i][n - 1] + nums[n]
                for j in range(i - 2, n):
                    if f[i - 1][j] + nums[n] > curMax:
                        curMax = f[i - 1][j] + nums[n]
                f[i][n] = curMax
        
        result = float("-infinity")
        for i in range(k - 1, len(nums)):
            if f[k][i] > result:
                result = f[k][i]
        
        return result
