# Jump Game II
# Given an array of non-negative integers, you are initially positioned at
# the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example
# Given array A = [2,3,1,1,4]
# The minimum number of jumps to reach the last index is 2. (Jump 1 step from
# index 0 to 1, then 3 steps to the last index.)
#

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        # write your code here
        if A == None or len(A) == 0:
            return -1
        
        n = len(A)
        start, end = 0, 0
        jumps = 0
        
        while end < n - 1:
            jumps += 1
            farest = end
            for i in range(farest + 1):
                if A[i] + i >= farest:  # Not 'end' here
                    farest = A[i] + i
            start = end + 1 # It doesn't matter if "start = end" here
            end = farest
            
        return jumps
