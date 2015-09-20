# Majority Number II
# Given an array of integers, the majority number is the number 
# that occurs more than 1/3 of the size of the array.
# Find it
#
# Example
# Given [1, 2, 1, 2, 1, 3, 3], return 1.
# Note
# There is only one majority number in the array.
#
# Challenge
# O(n) time and O(1) extra space.
#

class Solution:
    """
    @param nums: A list of integers
    @return: The majority number occurs more than 1/3
    """
    def majorityNumber(self, nums):
        # write your code here

        candidate1, count1 = None, 0
        candidate2, count2 = None, 0
        
        for i in range(len(nums)):
            
            if nums[i] == candidate1:
                count1 += 1
            elif nums[i] == candidate2:
                count2 += 1
                
            # Attention: The order of these "if"s can not be changed.
            # We have to check whether nums[i]==candidate1,2 first.
            # If we check whether count1,2==0 first, we may have 
            # candidate1 = candidate2 = 4 for the following list:
            # [1,1,1,1,2,2,3,3,4,4,4]
            
            elif count1 == 0:
                candidate1 = nums[i]
                count1 += 1
            elif count2 == 0:
                candidate2 = nums[i]
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
                
        count1, count2 = 0, 0
        for i in range(len(nums)):
            if nums[i] == candidate1:
                count1 += 1
            elif nums[i] == candidate2:
                count2 += 1
        if count1 >= count2:
            return candidate1
        else:
            return candidate2
