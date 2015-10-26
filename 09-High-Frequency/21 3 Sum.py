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
                        
                        
# If we don't want to check "[numbers[i], numbers[j], numbers[k]] not in result":
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                
                j, k = i + 1, n - 1
                while j < k:
                    sum = nums[i] + nums[j] + nums[k]
                    if sum == 0:
                        #and [nums[i], nums[j], nums[k]] not in result
                        result.append([nums[i], nums[j], nums[k]])
                        j = self.toNext(j, nums)
                        k = self.toPrev(k, nums)
                    elif sum < 0:
                        j += 1
                    else:
                        k -= 1
        
        return result
        
    def toNext(self, j, nums):
        i = j
        while nums[i] == nums[j] and i < len(nums) - 1:
            i += 1
        return i
        
    def toPrev(self, k, nums):
        i = k
        while nums[i] == nums[k] and i > 0:
            i -= 1
        return i
