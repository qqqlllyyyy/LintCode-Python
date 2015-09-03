# Minimum Path Sum
# Given a m x n grid filled with non-negative numbers, 
# find a path from top left to bottom right 
# which minimizes the sum of all numbers along its path.
#
# Note
# You can only move either down or right at any point in time.
#
#


class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        
        if grid == None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        result = [[grid[0][0] for i in range(n)] for j in range(m)]
        
        for i in range(1, m):
            result[i][0] = result[i - 1][0] + grid[i][0]
        for j in range(1, n):
            result[0][j] = result[0][j - 1] + grid[0][j]
            
        for i in range(1, m):
            for j in range(1, n):
                result[i][j] = min(result[i - 1][j], result[i][j - 1]) + grid[i][j]
        
        return result[m - 1][n - 1]
