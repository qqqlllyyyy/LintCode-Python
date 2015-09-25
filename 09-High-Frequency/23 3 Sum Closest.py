# 3 Sum Closest
# Given an array S of n integers, find three integers in S such that the
# sum is closest to a given number, target. Return the sum of the 
# three integers.
#
# Example
# For example, given array S = {-1 2 1 -4}, and target = 1. The sum that
# is closest to the target is 2. (-1 + 2 + 1 = 2).
#
# You may assume that each input would have exactly one solution.
# Challenge
# O(n^2) time, O(1) extra space

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        
        n = len(numbers)
        if n < 3: return 0
        numbers.sort()
        
        result = numbers[0] + numbers[1] + numbers[2]
        
        for i in range(n):
            # Two way pointers
            j = i + 1
            k = n - 1
            
            while j < k:
                sum = numbers[i] + numbers[j] + numbers[k]
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                    
                if sum == target:
                    return sum
                
                elif sum < target:
                    j += 1
                else: 
                    k -= 1
                    
        return result
                
