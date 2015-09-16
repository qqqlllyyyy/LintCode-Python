# k Sum
# Given n distinct positive integers, integer k (k <= n) and a number target.
# Find k numbers where sum is target. Calculate how many 
# solutions there are?
#
# Example
# Given [1,2,3,4], k = 2, target = 5.
# There are 2 solutions: [1,4] and [2,3].
# Return 2.

class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    
    # DP, time O(len(A) * k * target) only!
    
    def kSum(self, A, k, target):
        ans = [[[0 for i in range(target + 1)] for j in range(k + 1)] for K in range(len(A) + 1)]
        # table[i][j][t] denotes the number of ways to select,
        # from first i elements, j elements whose sum equals to t
        ans[0][0][0] = 1
        for I in range(len(A)):
            for J in range(k + 1):
                for K in range(target + 1):
                    # At least, we can use first "I" elements only 
                    ans[I + 1][J][K] = ans[I][J][K]
                    # If we use (I+1)th element:
                    if J - 1 >= 0 and K >= A[I]:
                        ans[I + 1][J][K] += ans[I][J - 1][K - A[I]]
        return ans[len(A)][k][target]
        
    
    # DFS
    
    def kSum(self, A, k, target):
        # write your code here
        self.result = []
        if A == None or len(A) == 0:
            return self.result
        path = []
        self.dfs(A, [], 0, target, k)
        return len(self.result)
        
    def dfs(self, A, path, start, target, k):
        if len(path) == k and target == 0:
            if path not in self.result:
                self.result.append(path)
                return
        
        for i in range(start, len(A)):
            if A[i] > target:
                return
            self.dfs(A, path + [A[i]], i + 1, target - A[i], k)
