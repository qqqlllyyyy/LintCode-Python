# Wood Cut 
# Given n pieces of wood with length L[i] (integer array). Cut them into
# small pieces to guarantee you could have equal or more than k pieces
# with the same length. What is the longest length you can get from the
# n pieces of wood? Given L & k, return the maximum length of the small pieces.
#
# Example
# For L=[232, 124, 456], k=7, return 114.
# You couldn't cut wood into float length.
#
# Challenge
# O(n log Len), where Len is the longest length of the wood.

class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        if sum(L) < k:
            return 0
        maxLength = max(L)
        
        start, end = 1, maxLength
        while start + 1 < end:
            mid = start + (end - start) / 2
            pieces = sum([l / mid for l in L])
            
            # Attention: Here can not be "pieces > k"
            # Beacuse if pieces == k, it may work for some larger value.
            # If we move "end" forward. We'll lost that largest value possible.
            # So we can only move "start".
            if pieces >= k:
                start = mid
            else:
                end = mid
        
        if sum([l / end for l in L]) >= k:
            return end
        return start
        
