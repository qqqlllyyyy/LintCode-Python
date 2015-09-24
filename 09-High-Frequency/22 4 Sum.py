# 4 Sum
# Given an array S of n integers, are there elements a, b, c, and d in S such
# that a + b + c + d = target? Find all unique quadruplets in the array which
# gives the sum of target.
#
# Example
# For example, given array S = {1 0 -1 0 -2 2}, and target = 0. A solution set is:
# (-1, 0, 0, 1), (-2, -1, 1, 2), (-2, 0, 0, 2)
#
# Note
# Elements in a quadruplet (a,b,c,d) must be in non-descending order.
# (ie, a <= b <= c <= d)
# The solution set must not contain duplicate quadruplets.
#

class Solution:
    """
    @param numbersbers : Give an array numbersbersbers of n integer
    @param target : you need to find four elements that's sum of target
    @return : Find all unique quadruplets in the array which gives the sum of 
              zero.
    """
    def fourSum(self ,numbers, target):
        # write your code here
        numbers.sort()
        if len(numbers) < 4: return []
        
        n = len(numbers)
        dict = {}
        result = []
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                sum1 = numbers[i] + numbers[j]
                
                if target - sum1 in dict:
                    for list2 in dict[target - sum1]:
                        
                        if list2 + [numbers[i], numbers[j]] not in result:
                            result.append(list2 + [numbers[i], numbers[j]])
                
            for j in range(i):
                if numbers[i] + numbers[j] in dict:
                    if [numbers[j], numbers[i]] not in dict[numbers[i] + numbers[j]]:
                        dict[numbers[i] + numbers[j]].append([numbers[j], numbers[i]])
                else:
                    dict[numbers[i] + numbers[j]] = [[numbers[j], numbers[i]]]
                
        return result

