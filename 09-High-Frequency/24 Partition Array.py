# Partition Array
# Given an array nums of integers and an int k, partition the array
# (i.e move the elements in "nums") such that:
# All elements < k are moved to the left
# All elements >= k are moved to the right
# Return the partitioning index, i.e the first index i nums[i] >= k.
#
# Example
# If nums = [3,2,2,1] and k=2, a valid answer is 1.
# Note
# You should do really partition in array nums instead of just counting
# the numbers of integers smaller than k.
# If all elements in nums are smaller than k, then return nums.length
#
# Challenge
# Can you partition the array in-place and in O(n)?

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        
        i = 0
        j = len(nums) - 1
        
        # Two way pointers
        while i <= j:
            while i <= j and nums[i] < k:
                i += 1
            while i <= j and nums[j] >= k:
                j -= 1
            
            if i <= j:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
        
        return i

