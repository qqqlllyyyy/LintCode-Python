# Climbing Stairs
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how 
# many distinct ways can you climb to the top?
#

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n == 0: return 1
        if n == 1: return 1
        result = [1 for i in range(n+1)]
        result[1] = 1
        for i in range(2, n+1):
            result[i] = result[i - 1] + result[i - 2]
        return result[n]
        
