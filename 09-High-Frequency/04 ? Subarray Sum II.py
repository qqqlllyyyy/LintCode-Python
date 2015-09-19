# Subarray Sum II
# Given an integer array, find a subarray where the sum of numbers 
# is between two given interval. Your code should return the 
# number of possible answer.
#
# Example
# Given [1,2,3,4] and interval = [1,3], return 4. The possible answers are:
# [0, 0], [0, 1], [1, 1], [2, 2]
#

class Solution:
    # @param {int[]} A an integer array
    # @param {int} start an integer
    # @param {int} end an integer
    # @return {int} the number of possible answer
    def subarraySumII(self, A, start, end):
        # Write your code here
        result = []
        
        for i in range(len(A)):
            for j in range(len(A)):
                sum = 0
                for k in range(i, j + 1):
                    sum += A[k]
                if start <= sum <= end:
                    result.append([i, j])
                    
                    
    # For the second method, I didn't count any result that can not 
    # be used. Why can't I pass the runtime test?
    # Is there a better way?
    def subarraySumII(self, A, start, end):
        result = 0
        dict = {0: [-1]}
        sum = 0
        for i in range(len(A)):
            sum += A[i]
            
            for j in range(sum - end, sum - start + 1):
                
                if j in dict:
                    result += len(dict[j])
            
            
            if sum not in dict:
                dict[sum] = [i]
            else:
                dict[sum].append(i)
        
        return result
        
