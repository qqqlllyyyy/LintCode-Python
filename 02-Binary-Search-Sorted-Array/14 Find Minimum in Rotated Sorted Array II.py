# Find Minimum in Rotated Sorted Array II
# Suppose a sorted array is rotated at some pivot unknown to you beforehand
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# Find the minimum element.
# The array may contain duplicates.
#
# Example
# Given [4,4,5,6,7,0,1,2] return 0
#
#
#


class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        
        if len(num) == 1:
            return num[0]
            
        start, end = 0, len(num) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if num[mid] > num[end]:
                start = mid
            elif num[mid] < num[end]: ## Have to use 'elif' here, not 'if' !!
                # Because you may change 'end' in the 2nd step and the changed
                # 'end' will also go through step 3.
                end = mid
            else:
                end -= 1 #Only dare to move one step
        
        # Note!! We have to use (start == 0) here, not (end == len(num)-1)
        # For example [1, 2, 2, 2, 2]
        if (start == 0) and (num[end] >= num[0]):
            return num[0]
        return num[end]
