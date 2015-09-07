# Backpack
# Given n items with size Ai, an integer m denotes the size of a 
# backpack. How full you can fill this backpack?
#
# Example
# If we have 4 items with size [2, 3, 5, 7], the backpack size is 
# 11, we can select [2, 3, 5], so that the max size we can fill this backpack is 10.
# If the backpack size is 12. we can select [2, 3, 7] so that we can fulfill the backpack.
# You function should return the max size we can fill in the given backpack.
#
# Note
# You can not divide any item into small pieces.
#
# Challenge
# O(n x m) time and O(m) memory.
# O(n x m) memory is also acceptable if you do not know how to optimize memory.


class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    
    def backPack(self, m, A):
        
        dp = [[False for i in range(m + 1)] for j in range(len(A) + 1)]
        dp[0][0] = True
        
        for i in range(1, len(A) + 1):
            dp[i][0] = True
        
        for i in range(1, len(A) + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= A[i - 1] and dp[i - 1][j - A[i - 1]]:# Remember here
                    # should be A[i - 1], not A[i]. We want the ith item in A
                    dp[i][j] = True
                    
        k = m
        while k >= 0:
            if dp[len(A)][k]:
                return k
            k -= 1
        return 0
