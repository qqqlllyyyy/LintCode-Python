# Merge Sorted Array
# Given two sorted integer arrays A and B, merge B into A as one sorted array.
#
# Example
# A = [1, 2, 3, empty, empty], B = [4, 5]
# After merge, A will be filled as [1, 2, 3, 4, 5]
#
# Note
# You may assume that A has enough space (size that is greater or equal to m + n)
# to hold additional elements from B. The number of elements initialized in A
# and B are m and n respectively.

class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        for i in range(n):
            A[m + i] = B[i];
        A.sort();

    
    """
    Python lists have a built-in sort() method that modifies the list in-place
    and a sorted() built-in function that builds a new sorted list from an iterable.
    """
