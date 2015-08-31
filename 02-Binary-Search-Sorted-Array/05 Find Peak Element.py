# Find Peak Element
# There is an integer array which has the following features:
# 1. The numbers in adjacent positions are different.
# 2. A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
# We define a position P is a peek if:
# A[P] > A[P-1] && A[P] > A[P+1]
# Find a peak element in this array. Return the index of the peak.
#
# Example
# Given [1, 2, 1, 3, 4, 5, 7, 6]
# Return index 1 (which is number 2) or 6 (which is number 7)
#
# Time complexity O(logN)


class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if (A[mid - 1] < A[mid]) and (A[mid + 1] < A[mid]):
                return mid;
            if A[mid + 1] < A[mid]:
                end = mid;
            else:
                start = mid;
