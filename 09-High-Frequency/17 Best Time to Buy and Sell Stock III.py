# Best Time to Buy and Sell Stock III
# Say you have an array for which the ith element is the price
# of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete
# at most two transactions.
#
# Example
# Given an example [4,4,6,1,1,4,2,5], return 6.
#
# Note
# You may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).
#

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    # My way, not perfect in time.
    def maxProfit(self, prices):
        # write your code here
        result = 0
        for i in range(len(prices)):# Note here is not "len(prices) - 1"
        # Because the right side can be [], for example, prices = [1, 2]
            left = self.highest(prices[ : i + 1])
            right = self.highest(prices[i + 1 : ])
            result = max(result, left + right)
        return result
        
        
    
    def highest(self, nums):
        if len(nums) <= 1:
            return 0
        
        maxProfit = 0
        minSoFar = nums[0]
        for i in range(1, len(nums)):
            maxProfit = max(maxProfit, nums[i] - minSoFar)
            minSoFar = min(minSoFar, nums[i])
        return maxProfit

    """
        Try to do it using O(n) method like "Maximum Subarray II" next time.
    """
