# Binary Search
# For a given sorted array (ascending order) and a target number, 
# find the first index of this number in O(log n) time complexity.
# If the target number does not exist in the array, return -1.
#
# If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.
#

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
       
        if (target == None):
            return -1;
        
        start = 0; end = len(nums);
        while start + 1 < end:
            mid = start + (end - start)/2;
            if nums[mid] >= target:
                end = mid;
            else:
                start = mid;
        
        if nums[start] == target:
            return start;
        else:
            if nums[end] == target:
                return end;
            else:
                return -1;
