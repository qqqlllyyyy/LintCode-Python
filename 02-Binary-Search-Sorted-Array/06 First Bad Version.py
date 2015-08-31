# tests. Find the first bad version.
# You can call isBadVersion to help you determine which version
# is the first bad one. The details interface can be found in the 
# code's annotation part.
#
# Example
# isBadVersion(3) -> false
# isBadVersion(5) -> true
# isBadVersion(4) -> true
# Here we are 100% sure that the 4th version is the first bad version.
#
# You should call isBadVersion as few as possible.
#

#class VersionControl:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use VersionControl.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        
        start = 1; end = n;
        while start + 1 < end:
            mid = start + (end - start)/2;
            if VersionControl.isBadVersion(mid):
                end = mid;
            else:
                start = mid;
        
        if VersionControl.isBadVersion(start):
            return start;
        if VersionControl.isBadVersion(end):
            return end;
