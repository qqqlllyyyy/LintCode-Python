# Median of two Sorted Arrays Show result
# There are two sorted arrays A and B of size m and n respectively. 
# Find the median of the two sorted arrays.
#
# Example
# Given A=[1,2,3,4,5,6] and B=[2,3,4,5], the median is 3.5.
# Given A=[1,2,3] and B=[4,5], the median is 3.
#
# The overall run time complexity should be O(log (m+n)).



class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    ## Method in Chinese: http://chaoren.is-programmer.com/posts/42890.html
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findKth(A, B, n / 2 + 1)
        else:
            smaller = self.findKth(A, B, n / 2)
            bigger = self.findKth(A, B, n / 2 + 1)
            return (smaller + bigger) / 2.0
            
    def findKth(self, A, B, k):
        # Be careful about these three boundary cases
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])
            
        if len(A) >= k/2:
            a = A[k / 2 - 1]
        else:
            a = None
            
        if len(B) >= k / 2:
            b = B[k / 2 - 1]
        else:
            b = None
            
        if (b is None) or ((a is not None) and (b > a)):
            return self.findKth(A[k / 2:], B, k - k / 2)
            # !!! You can not use (k/2) instead of (k - k/2) here, if k = 5, k/2=2, k-k/2=3
        return self.findKth(A, B[k / 2:], k - k / 2)
