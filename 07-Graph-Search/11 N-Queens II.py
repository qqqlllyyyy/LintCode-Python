# N-Queens II
# Follow up for N-Queens problem.
# Now, instead outputting board configurations, return the total 
# number of distinct solutions.
#
class Solution:
    """
    Calculate the total number of distinct N-Queen solutions.
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """

    def totalNQueens(self, n):
        # write your code here
        self.result = []
        if n <= 0:
            return self.result
        self.dfs(n, [])
        return len(self.result)
    
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
    


