# Maximum Subarray Difference
# Given an array with integers.
# Find two non-overlapping subarrays A and B, which |SUM(A) - SUM(B)|
# is the largest.
# Return the largest difference.
#
# Example
# For [1, 2, -3, 1], return 6
# Note
# The subarray should contain at least one number
# Challenge
# O(n) time and O(n) space.
#
class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two
             Subarrays
    """
    # My way, not perfect in time.
    def maxDiffSubArrays(self, nums):
        # write your code here
        if nums == None or len(nums) <= 1: return None
        result = 0
        for i in range(len(nums) - 1):
            leftMin = self.findMin(nums[ : i + 1])
            leftMax = self.findMax(nums[ : i + 1])
            rightMin = self.findMin(nums[i + 1 : ])
            rightMax = self.findMax(nums[i + 1 : ])
            result = max(result, abs(leftMin - rightMax), abs(leftMax - rightMin))
        return result
        

    def findMax(self, nums):
        result = float("-infinity")
        sum, minSoFar = 0, 0
        for i in range(len(nums)):
            sum += nums[i]
            result = max(result, sum - minSoFar)
            minSoFar = min(minSoFar, sum)
        return result
        
    def findMin(self, nums):
        reverse = []
        for i in range(len(nums)):
            reverse.append(-nums[i])
        result = self.findMax(reverse)
        return -result

    """
        Try to do it using O(n) method like "Maximum Subarray II" next time.
    """
