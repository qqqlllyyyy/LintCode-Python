# k Sum II
# Given n unique integers, number k (1<=k<=n)  and target. Find all 
# possible k integers where their sum is target.
#
# Example
# Given [1,2,3,4], k=2, target=5, [1,4] and [2,3] are possible solutions.
#

class Solution:
    """
    @param A: An integer array.
    @param k: A positive integer (k <= length(A))
    @param target: Integer
    @return a list of lists of integer 
    """
    def kSumII(self, A, k, target):
        # write your code here
        self.result = []
        if A == None or len(A) == 0:
            return self.result
        A.sort()
        self.dfs([], target, 0, A, k)
        return self.result
    
    def dfs(self, path, target, start, A, k):
        if target == 0 and len(path) == k and path not in self.result:
            self.result.append(path)
        for i in range(start, len(A)):
            if A[i] > target:
                return
            self.dfs(path + [A[i]], target - A[i], i + 1, A, k)
            
