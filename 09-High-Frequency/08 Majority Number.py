# Majority Number
# Given an array of integers, the majority number is the number 
# that occurs more than half of the size of the array. Find it.
#
# Example 
# Given [1, 1, 1, 1, 2, 2, 2], return 1
#
# Challenge
# O(n) time and O(1) extra space

class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    
    
    def majorityNumber(self, nums):
        # write your code here
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            elif candidate == num:
                count += 1
            else:
                count -= 1
        return candidate
