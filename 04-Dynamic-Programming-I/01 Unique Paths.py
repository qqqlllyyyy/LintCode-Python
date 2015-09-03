# Unique Paths
# A robot is located at the top-left corner of a m x n grid 
# (marked 'Start' in the diagram below).
# The robot can only move either down or right at any 
# point in time. The robot is trying to reach the bottom-
# right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?
#




class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 

    def uniquePaths(self, m, n):
        
        dp=[[0 for index in range(n)] for index in range(m)]
        # Remember to loop through n first in the code above,
        # since we want to have m rows, which means we need to
        # have m sub-lists inside of the bigger list

        
        for row in range(m):  
            dp[row][0]=1  
        for col in range(n):  
            dp[0][col]=1  
        for row in range(1,m):  
            for col in range(1,n):  
                dp[row][col]=dp[row-1][col]+dp[row][col-1]  
        return dp[m-1][n-1] 
