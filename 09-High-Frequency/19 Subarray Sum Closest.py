# Subarray Sum Closest
# Given an integer array, find a subarray with sum closest to zero. 
# Return the indexes of the first number and last number.
#
# Example
# Given [-3, 1, 1, -3, 5], return [0, 2], [1, 3], [1, 1], [2, 2] or [0, 4]
#
# Challenge
# O(nlogn) time

"""We want to use sorting once we see O(nlogn) time complexity"""
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        
        if nums == None or len(nums) == 0: return None
        if len(nums) == 1: return 0, 0
        
        # Find the sum list
        sumList = [nums[0] for i in range(len(nums))]
        for i in range(1, len(nums)):
            sumList[i] = sumList[i-1] + nums[i]

        # We need to store the information about index.
        # Since we will lost info of index after sorting the sum list
        dict = {}
        for i in range(len(sumList)):
            if sumList[i] in dict:
                return min(i, dict[sumList[i]]) + 1, max(i, dict[sumList[i]])
                # Don't forget "+1" here:
                # If sum[0-5] = sum[0-9], that means sum[6-9]=0, not sum[5-9]
            else:
                dict[sumList[i]] = i
          
        sumList.sort()
        
        
        start, diff = 0, float("infinity")
        for i in range(len(sumList) - 1):
            if sumList[i + 1] - sumList[i] < diff:
                diff = sumList[i + 1] - sumList[i]
                start = i
        
        minValue = min(dict[sumList[start]], dict[sumList[start + 1]])
        maxValue = max(dict[sumList[start]], dict[sumList[start + 1]])
        return minValue + 1, maxValue
        # Don't forget "+1", either.
        
        
