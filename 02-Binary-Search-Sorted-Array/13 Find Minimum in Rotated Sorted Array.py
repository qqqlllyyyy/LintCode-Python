# Find Minimum in Rotated Sorted Array
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# Find the minimum element.
#
# Example
# Given [4, 5, 6, 7, 0, 1, 2] return 0
#
# Note
# You may assume no duplicate exists in the array.


class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        if(len(num) == 0):
            return num[0]
        
        start, end = 0, len(num) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if num[mid] > num[start]:
                start = mid
            else:
                end = mid
                
        if (end == len(num) - 1) and (num[end] > num[start]):
            # Remember the conditions
            return num[0]
        return num[end]
