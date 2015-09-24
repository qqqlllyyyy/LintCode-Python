# 3 Sum 
# Given an array S of n integers, are there elements a, 
# b, c in S such that a + b + c = 0? Find all unique
# triplets in the array which gives the sum of zero.
#
# Example
# For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
# [-1, 0, 1], [-1, -1, 2]
# Note
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
# The solution set must not contain duplicate triplets.

class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers.sort() # Don't forget to sort
        n = len(numbers)
        result = []
        
        for i in range(n - 2):
            if i == 0 or numbers[i] != numbers[i - 1]:
                j = i + 1
                k = n - 1
                
                while j < k:
                    sum = numbers[i] + numbers[j] + numbers[k]
                    if sum == 0 and [numbers[i], numbers[j], numbers[k]] not in result:
                        result.append([numbers[i], numbers[j], numbers[k]])
                        j += 1
                        k -= 1
                    elif sum < 0:
                        j += 1
                    else:
                        k -= 1
        return result
                        
