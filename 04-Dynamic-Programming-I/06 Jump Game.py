# Jump Game
# Given an array of non-negative integers, you are 
# initially positioned at the first index of the array.
# Each element in the array represents your maximum 
# jump length at that position.
# Determine if you are able to reach the last index.
#
# Example
# A = [2,3,1,1,4], return true.
# A = [3,2,1,0,4], return false.
#

class Solution:
    # @param A, a list of integers
    # @return a boolean
    
# Dynamic Programming: O(n^2) time
    def canJump(self, A):
        
        if len(A) == 0:
            return False
        n = len(A)
        result = [False for i in range(n)]
        result[0] = True
        
        for i in range(1, n):
            for j in range(i):
                if result[j] and j + A[j] >= i:
                    result[i] = True
                    break
        
        return result[n - 1]
        

# Greedy Method: O(n) time
    def canJump(self, A):
        
        if A == None or len(A) == 0:
            return False
        farest = 0
        n = len(A)
        for i in range(n):
            if i + A[i] > farest and i <= farest: # Don't forget the second condition here.
                farest = i + A[i]
        return farest >= n -1 
