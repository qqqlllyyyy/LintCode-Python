# Sort Colors II
# Given an array of n objects with k different colors (numbered from 1 to k),
# sort them so that objects of the same color are adjacent, with the colors
# in the order 1, 2, ... k.
#
# Example
# Given colors=[3, 2, 2, 1, 4], k=4, your code should sort colors in-place
# to [1, 2, 2, 3, 4].
#
# Note
# You are not suppose to use the library's sort function for this problem.
#
# Challenge
# A rather straight forward solution is a two-pass algorithm using counting
# sort. That will cost O(k) extra memory. Can you do it without using extra
# memory?

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        n = 0
        for i in range(k - 1):
            n = self.sort(colors, i + 1, n)
        
    def sort(self, nums, flag, index):
        start, end = index, len(nums) - 1
        
        while start <= end:
            while start <= end and nums[start] == flag:
                start += 1
            while start <= end and nums[end] != flag:
                end -= 1
            
            if start <= end:
                
                temp = nums[end]
                nums[end] = nums[start]
                nums[start] = temp
                start += 1
                end -= 1
                
        return start
