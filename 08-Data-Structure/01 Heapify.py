# Heapify
# Given an integer array, heapify it into a min-heap array.
# For a heap array A, A[0] is the root of heap, and for each A[i],
# A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right
# child of A[i].
#
# Example
# Given [3,2,1,4,5], return [1,2,3,4,5] or any legal heap array.
#
# Challenge
# Given [3,2,1,4,5], return [1,2,3,4,5] or any legal heap array.

class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        # write your code here
        
        i = len(A) / 2
        while i >= 0:
            self.shiftDown(A, i)
            i -= 1
    
    def shiftDown(self, A, i):
        while i < len(A):
            smallest = i
            if 2 * i + 1 < len(A) and A[2 * i + 1] < A[smallest]:
                smallest = 2 * i + 1
            if 2 * i + 2 < len(A) and A[2 * i + 2] < A[smallest]:
                smallest = 2 * i + 2
            if smallest == i:
                break
            
            temp = A[smallest]
            A[smallest] = A[i]
            A[i] = temp
            
            i = smallest
                
