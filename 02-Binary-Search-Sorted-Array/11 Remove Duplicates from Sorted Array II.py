# Remove Duplicates from Sorted Array II
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
# Example
# Given sorted array A = [1,1,1,2,2,3],
# Your function should return length = 5, and A is now [1,1,2,2,3].
#


class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        if len(A) <= 2:
            return len(A)
            
        slow = 1
        for fast in range(2, len(A)):
            if A[fast] != A[slow - 1]:
                A[slow + 1] = A[fast]
                slow += 1
        
        return slow + 1
