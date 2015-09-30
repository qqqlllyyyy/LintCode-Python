# Search a 2D Matrix
# Write an efficient algorithm that searches for a value in an m x n matrix.
# Write an efficient algorithm that searches for a value in an m x n matrix.
# 1. Integers in each row are sorted from left to right.
# 2. The first integer of each row is greater than the last integer of the previous row.
#
# Example
# [
#    [1, 3, 5, 7],
#    [10, 11, 16, 20],
#    [23, 30, 34, 50]
# ]
# Given target = 3, return true.
# O(log(n) + log(m)) time

class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix == None or len(matrix) == 0: return False
        start, end = 0, len(matrix) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if target < matrix[mid][0]:
                end = mid
            else:
                start = mid
        return self.searchList(matrix[start], target) or self.searchList(matrix[end], target)
        
        
        

    def searchList(self, list1, target):
        if list1 == None or len(list1) == 0: return False
        start, end = 0, len(list1) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if list1[mid] == target:
                return True
            if target < list1[mid]:
                end = mid
            else:
                start = mid
        if target == list1[start] or target == list1[end]:
            return True
        return False
