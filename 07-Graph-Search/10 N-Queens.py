# N-Queens
# The n-queens puzzle is the problem of placing n queens on an 
# n*n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# Each solution contains a distinct board configuration of the n-
# queens' placement, where 'Q' and '.' both indicate a queen and 
# an empty space respectively.
#
# Example
# There exist two distinct solutions to the 4-queens puzzle:
# [
#  [".Q..", // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#  ["..Q.", // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Challenge
# Can you do it without recursion?
#

class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        self.result = []
        if n <= 0:
            return self.result
        self.dfs(n, [])
        return self.result
    
    # Main DFS step
    def dfs(self, n, cols):
        if len(cols) == n:
            self.result.append(self.drawChessboard(cols))
            return 
        
        for col in range(n):
            if self.isValid(cols, col):
                self.dfs(n, cols + [col])
        
    # Transfer a string of numbers into a "chessboard" list         
    def drawChessboard(self, cols):
        chessboard = ['' for i in range(len(cols))]
        for i in range(len(cols)):
            for j in range(len(cols)):
                if j == cols[i]:
                    chessboard[i] += 'Q'
                else:
                    chessboard[i] += '.'
        return chessboard
    
    # Test whether new "col" is valid
    def isValid(self, cols, col):
        row = len(cols)
        for i in range(row):
            # same column
            if cols[i] == col:
                return False
            # right-top to left-bottom
            if i - cols[i] == row - col:
                return False
            # left-top to right-bottom
            if i + cols[i] == row + col:
                return False
        return True

"""How to do it without recursion?"""
    
