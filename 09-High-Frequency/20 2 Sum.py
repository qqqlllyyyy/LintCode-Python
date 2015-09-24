# 2 Sum 
# Given an array of integers, find two numbers such that they add up to
# a specific target number.
# The function twoSum should return indices of the two numbers such
# that they add up to the target, where index1 must be less than index2.
# Please note that your returned answers (both index1 and index2) are NOT
# zero-based.
#
# Example
# numbers=[2, 7, 11, 15], target=9
# return [1, 2]
# Either of the following solutions are acceptable:
# O(n) Space, O(nlogn) Time
# O(n) Space, O(n) Time

class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        
        """ Have a dictionary to store values and their indexes"""
        dict = {}
        for i in range(len(numbers)):
            if target - numbers[i] in dict:
                return dict[target - numbers[i]] + 1, i + 1
            else:
                dict[numbers[i]] = i
        return []
