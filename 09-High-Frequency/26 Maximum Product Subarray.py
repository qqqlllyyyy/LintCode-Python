# Maximum Product Subarray
# Find the contiguous subarray within an array (containing at least
# one number) which has the largest product.
#
# Example
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
#

class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        # write your code here
        # O(n) time and O(1) space
        
        if nums == None or len(nums) == 0: return 0
        
        n = len(nums)
        
        # We need to record 3 numbers: 
        # 1. maximum product so far
        # 2. max positive product using the most recent number(ith).
        # 3. min negative product using the most recent number(ith).
        maxProduct = nums[0]
        negativeProduct = nums[0]
        positiveProduct = nums[0]
        
        for i in range(1, n):
            a = negativeProduct * nums[i]
            b = positiveProduct * nums[i]
            
            negativeProduct = min(a, b, nums[i])
            positiveProduct = max(a, b, nums[i])
            maxProduct = max(maxProduct, positiveProduct)
            
        return maxProduct
