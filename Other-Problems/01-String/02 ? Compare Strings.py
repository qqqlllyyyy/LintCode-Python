# Compare Strings
# Compare two strings A and B, determine whether A contains all of
# the characters in B.
# The characters in string A and B are all Upper Case letters.
#
# Example
# For A = "ABCD", B = "ACD", return true.
# For A = "ABCD", B = "AABC", return false.
#
# Note
# The characters of B in A are not necessary continuous or ordered.

"""Can not pass. Is there anything wrong with my code?"""

class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        if B == "": return True
        
        dict1 = {}
        Upperset = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for i in Upperset:
            dict1[i] = 0

        for i in range(len(B)):
            dict1[B[i]] += 1
        for i in range(len(A)):
            dict1[A[i]] -= 1
            if dict1[A[i]] < 0:
                return False
        
        return True
