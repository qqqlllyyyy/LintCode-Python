# Find Peak Element II
# There is an integer matrix which has the following features:

#    The numbers in adjacent positions are different.
#    The matrix has n rows and m columns.
#    For all i < m, A[0][i] < A[1][i] && A[n - 2][i] > A[n - 1][i].
#    For all j < n, A[j][0] < A[j][1] && A[j][m - 2] > A[j][m - 1].

# We define a position P is a peek if:
# A[j][i] > A[j+1][i] && A[j][i] > A[j-1][i] &&
# A[j][i] > A[j][i+1] && A[j][i] > A[j][i-1]
# Find a peak element in this matrix. Return the index of the peak.
#
# Example
# Given a matrix:
# [
#  [1 ,2 ,3 ,6 ,5],
#  [16,41,23,22,6],
#  [15,17,24,21,7],
#  [14,18,19,20,10],
#  [13,14,11,10,9]
# ]
# return index of 41 (which is [1,1]) or index of 24 (which is [2,2])
#
# Challenge
# Solve it in O(n+m) time.
# If you come up with an algorithm that you thought it is O(n log m) or
# O(m log n), can you prove it is actually O(n+m) or propose a similar but
# O(n+m) algorithm?

"""
    The main thing needed to know is that if A[mid][col] < A[mid + 1][col],
    we can prove that there must be at least one peak on the downside.
"""
class Solution:
    #@param A: An list of list integer 
    #@return: The index of position is a list of integer, for example [2,2]
    def findPeakII(self, A):
        # write your code here
        low, high = 1, len(A) - 2
        while low <= high:
            mid = low + (high - low) / 2
            col = self.helper(mid, A)
            if A[mid][col] < A[mid + 1][col]:
                low = mid + 1 # Why can not use 'low = mid' here?
                # Because we may need "low == high" in the end.
                # If low = high - 1, then low = mid, we'll never move on.
            elif A[mid][col] < A[mid - 1][col]:
                high = mid - 1
            else:
                return mid, col

    def helper(self, row, A):
        maxCol = 0
        for i in range(len(A[row])):
            if A[row][i] > A[row][maxCol]:
                maxCol = i
        return maxCol
