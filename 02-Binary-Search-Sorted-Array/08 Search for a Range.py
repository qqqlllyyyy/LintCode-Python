# Search for a Range
# Given a sorted array of n integers, find the starting and ending 
# position of a given target value.
# If the target is not found in the array, return [-1, -1].
#
# Example
# Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4].
# O(log n) time.
#
#

# O(log n) time.
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        
        if (A == None) or (len(A) == 0):
            return [-1, -1]
        
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        ## Think carefully, which one should come first, 'start' or 'end'?
        if A[start] == target:
            result0 = start
        elif A[end] == target:
            result0 = end
        else:
            return [-1, -1]
            
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            result1 = end
        else:
            result1 = start
        
        return [result0, result1]


# O(n) Time

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        
        if (A == None) or (len(A) == 0):
            return [-1, -1]
        # Find the first position
        i = 0
        while i < len(A):
            if A[i] == target:
                result0 = i
                break ## Dont's forget this 'break'
            else:
                i += 1
                
        if i == len(A):
            return [-1, -1]
        # Find the last position
        i = 0
        while i < len(A) - 1:
            if (A[i] == target) and (A[i+1] != target):
                result1 = i
                break
            else:
                i = i + 1
        
        if (i == len(A) - 1) and (A[len(A) - 1] == target):
            result1 = len(A) - 1
            
        return [result0, result1]
