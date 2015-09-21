# Best Time to Buy and Sell Stock
# Say you have an array for which the ith element is the price of a 
# given stock on day i.
# If you were only permitted to complete at most one transaction 
# (ie, buy one and sell one share of the stock), design an algorithm 
# to find the maximum profit.
#
# Example
# Given an example [3,2,3,1,2], return 1
#
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if prices == None or len(prices) == 0: return 0
        
        # Different from the problem "Maximum Subarray", 
        # "minSoFar" can not be set to 0 because it will never
        # change for a list of positive integers.
        minSoFar = prices[0]
        result = float("-infinity")
        for i in range(len(prices)):
            result = max(result, prices[i] - minSoFar)
            minSoFar = min(minSoFar, prices[i])
            
        return result
