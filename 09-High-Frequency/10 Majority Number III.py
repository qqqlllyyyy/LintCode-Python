# Majority Number III
# Given an array of integers and a number k, the majority number is 
# the number that occurs more than 1/k of the size of the array.
# Find it
#
# Example
# Given [3,1,2,3,2,3,3,4,4,4] and k=3, return 3.
# Note
# There is only one majority number in the array.
# Challenge
# O(n) time and O(k) extra space
#
class Solution:
    """
    @param nums: A list of integers
    @param k: As described
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # write your code here
        
        counters = {}
        
        for i in nums:
            if i not in counters:
                counters[i] = 1
            else:
                counters[i] += 1
            
            if len(counters) >= k:
                self.removeKey(counters)
                
        if len(counters) == 0:
            return None # It seems that here can alse return float("-infinity")
           
        # Reset values to 0 
        for i in counters:
            counters[i] = 0
        for i in nums:
            if i in counters:
                counters[i] += 1
        
        # Find the max key
        maxCounter, maxKey = 0, 0
        for i in counters:
            if counters[i] > maxCounter:
                maxCounter = counters[i]
                maxKey = i
        
        return maxKey
        
    
    def removeKey(self, counters):
        
        for i in counters.keys(): 
            # Attention! Here we can not just use "for i in counters"
            # Because then "counters" may change size during iteration!!
            counters[i] -= 1
            if counters[i] == 0:
                del counters[i]
        
