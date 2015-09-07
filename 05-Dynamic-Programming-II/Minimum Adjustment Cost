# Minimum Adjustment Cost
# Given an integer array, adjust each integers so that the difference 
# of every adjacent integers are not greater than a given number target.
# If the array before adjustment is A, the array after adjustment is B, 
# you should minimize the sum of |A[i]-B[i]|
#
# Example
# Given [1,4,2,3] and target = 1, one of the solutions is [2,3,2,3],
# the adjustment cost is 2 and it's minimal.
# Return 2.
#
# Note
# You can assume each number in the array is a positive integer and not
# greater than 100.
#

"""
dp[i][j] is the adjustment cost of adjusting the first i integers
of A and the last integer after adjusting is 'j + 1'.
"""

class Solution:
    # @param A: An integer array.
    # @param target: An integer.
    def MinAdjustmentCost(self, A, target):
        # write your code here
           
        dp = [[0 for i in range(100)] for j in range(len(A) + 1)]  
        
        for i in range(1, len(A) + 1):
            for j in range(100):
                
                dp[i][j] = float("infinity")
                lowerBound = max(1, j + 1 - target)
                upperBound = min(100, j + 1 + target)
                for p in range(lowerBound, upperBound + 1):
                    dp[i][j] = min(dp[i][j], dp[i - 1][p - 1] + abs(A[i - 1] - (j + 1)))
                    
                    
        result = float("infinity")
        for j in range(100):
            result = min(result, dp[len(A)][j])
            
        return result
