# Recover Rotated Sorted Array
# Given a rotated sorted array, recover it to sorted array in-place.
#
# Example
# [4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]
#
# For example, the orginal array is [1,2,3,4], The rotated array
# of it can be [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]


class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    # O(1) extra space
    def reverse(self, A, m, n):
        while m < n:
            temp = A[n];
            A[n] = A[m];
            A[m] = temp;
            m += 1; n -= 1;
        
    def recoverRotatedSortedArray(self, nums):
        # Can use (not isinstance(nums, list)) to make sure this is a list.
        # Can not use (!isinstance(nums, list))
        if (nums == None) or (len(nums) <= 1):
            return
        
        k = None;
        for i in range(len(nums) - 2):
            if nums[i + 1] < nums[i]:
                k = i;
        
        if k != None:
            self.reverse(nums, 0, k);
            self.reverse(nums, k + 1, len(nums) - 1);
            self.reverse(nums, 0, len(nums) - 1);

            


    # O(n) extra space.
    def recoverRotatedSortedArray(self, nums):
        i = 0;
        A = nums * 1; # I forgot this step at first. Then A will not be defined after the 'while' loop for [1, 2, 3, 4, 5]
        while i < len(nums) - 1:
            if nums[i + 1] < nums[i]:
                A = nums[i+1:] + nums[:i+1];
            i = i + 1;
            
        for i in range(len(nums)):
            nums[i] = A[i];
