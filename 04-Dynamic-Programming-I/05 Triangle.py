# Triangle
# Given a triangle, find the minimum path sum from top 
# to bottom. Each step you may move to adjacent 
# numbers on the row below.
#
# Note
# Bonus point if you are able to do this using only O(n) extra space, where n is 
# the total number of rows in the triangle.



class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        
        if triangle == None or len(triangle) == 0:
            return 0
        
        n = len(triangle)
        result = [[0 for i in range(n)] for j in range(n)]
        
        for i in range(n):
            result[n - 1][i] = triangle[n - 1][i]
        
        i = n - 2
        while i >= 0:
            for j in range(i + 1): # Notice here is range(i+1), since j can be i. 
                result[i][j] = min(result[i + 1][j], result[i + 1][j + 1]) + triangle[i][j]
            i -= 1
        
        return result[0][0]
