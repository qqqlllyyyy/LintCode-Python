# Longest Increasing Subsequence
# Given a sequence of integers, find the longest increasing subsequence (LIS).
# You code should return the length of the LIS.
#
# Example
# For [5, 4, 1, 2, 3], the LIS  is [1, 2, 3], return 3
# For [4, 2, 4, 5, 3, 7], the LIS is [4, 4, 5, 7], return 4
# Time complexity O(n^2) or O(nlogn)
#
# The longest increasing subsequence problem is to find a subsequence of a
# given sequence in which the subsequence's elements are in sorted order,
# lowest to highest, and in which the subsequence is as long as possible.
# This subsequence is not necessarily contiguous, or unique.


class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):

        # write your code here
        n = len(nums)
        
        if n <= 1: return n
        
        result = [1 for i in range(n)]
        for i in range(1, n):
            
            for j in range(i):
                if nums[j] <= nums[i]:
                    result[i] = max(result[i], result[j] + 1)
        
        maxLength = 1
        for i in range(n):
            maxLength = max(maxLength, result[i])
        return maxLength
