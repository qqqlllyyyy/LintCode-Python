# Search Insert Position
# Given a sorted array and a target value, return the index if the
# target is found. If not, return the index where it would be if it were
# inserted in order.
# You may assume NO duplicates in the array.
#
# Example
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0


class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """

    # O(log(n)) time
    
    def searchInsert(self, A, target):
        # write your code here
        
        if (len(A) == 0):
            return 0;
            
        start = 0; end = len(A) - 1;

        if (target > A[len(A) - 1]):
            return len(A);
        
        while start + 1 < end:
            mid = (start + end)/2;
            if A[mid] == target:
                return mid;
            if A[mid] > target:
                end = mid;
            else:
                start = mid;
            
        if A[start] >= target:
            return start;
        if A[end] >= target:
            return end;


      # O(n) time
      def searchInsert(self, A, target):
        
        if len(A) == 0:
            return 0;
            
        for i in range(len(A)):
            if A[i] >= target:
                return i;
        return len(A);
