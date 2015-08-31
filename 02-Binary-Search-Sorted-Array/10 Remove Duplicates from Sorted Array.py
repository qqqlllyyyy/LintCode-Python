# Remove Duplicates from Sorted Array
# Given a sorted array, remove the duplicates in place such that each 
# element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in 
# place with constant memory.
#
# Example
# Given input array A = [1,1,2],
# Your function should return length = 2, and A is now [1,2].
#
# ?? Didn't remove A[slow+1:] ??


class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        if (len(A) == 0):
            return 0

        # Use two indexes: slow and fast
        slow = 0;
        for fast in range(len(A)):
            if A[fast] == A[slow]:
                continue
            else:
                slow += 1;
                A[slow] = A[fast]
        
        return slow + 1
