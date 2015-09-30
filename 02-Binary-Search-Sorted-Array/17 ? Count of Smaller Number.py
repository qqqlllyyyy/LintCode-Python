# Count of Smaller Number
# Give you an integer array (index from 0 to n-1, where n is the size of
# this array, value from 0 to 10000) and an query list. For each query, give
# you an integer, return the number of element in the array that are smaller
# that the given integer.
#
# Example
# For array [1,2,7,8,5], and queries [1,8,5], return [0,4,2]
#
# We suggest you finish problem Segment Tree Build and Segment Tree Query II first.
#
# Challenge
# Could you use three ways to do it.
# 
# 1. Just loop
# 2. Sort and binary search
# 3. Build Segment Tree and Search.

class Solution:
    """
    @param A: A list of integer
    @return: The number of element in the array that 
             are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        A.sort()
        result = []
        for q in queries:
            result.append(self.countSmaller(A, q))
        return result
        
    
    def countSmaller(self, A, q):
        if len(A) == 0 or A[len(A) - 1] < q:
            return len(A)
        
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            
            # Be careful here. Since we may have duplicate 'q',
            # We have to move 'end' forward if q == A[mid].
            # Otherwise we may lost information of first position
            # where q appeared.
            '''if q == A[mid]:
                return mid'''
            if q <= A[mid]:
                end = mid
            else:
                start = mid
        # Check start first
        if A[start] >= q:
            return start
        if A[end] >= q:
            return end
        #return end + 1 # Have to include this line?

    """
        ? Segment Tree Method ?
    """

        
        
