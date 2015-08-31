# Search in Rotated Sorted Array II
# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
# Would this affect the run-time complexity? How and why?
# Write a function to determine if a given target is in the array.
#
# Return True or False


class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """
    # O(logn)
    def search(self, A, target):
        
        if len(A) == 0:
            return False
        if len(A) == 1:
            if A[0] == target:
                return True
            return False
            
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                return True
                
            # Be really careful here
            if A[end] > A[mid]:
                if A[mid] < target < A[end]:
                    start = mid
                else:
                    end = mid
            elif A[end] < A[mid]:
                if A[start] <= target < A[mid]:
                    end = mid
                else:
                    start = mid
                
            else:
                end -= 1
                
        if (A[start] == target) or (A[end] == target):
            return True
        return False
      
                
      # O(n)
      def search(self, A, target):
        
          if len(A) == 0:
              return False
        
          for i in range(len(A)):
              if target == A[i]:
                  return True
        
          return False"""               
