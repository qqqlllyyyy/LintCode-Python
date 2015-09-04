# Palindrome Partitioning II
# Given a string s, cut s into some substrings such that every substring is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# Example
# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
#

class Solution:
    # @param s, a string
    # @return an integer
    

    # We use dynamic programming twice, first we obtain the matrix that indicates if an element is palindrome (cf. Palindrome Partioning I). Then, we calculate the minCut till the element i, as follows:
    # If isPalindrome(0,i) then minCut[i]=0
    # else minCut[i] = min( minCut[j]+1 && isPalindrome(i,j))
    
    def minCut(self, s):

        # Build up a real value table to check whether a word is palindrome
        isPalindrome=[]
        for start in range(0, len(s)):
            isPalindrome.append([])
            
        for length in range(0,len(s)):
            for start in range(0, len(s)-length):
                if length == 0:
                    isPalindrome[start].append(True)
                elif length == 1:
                    isPalindrome[start].append(s[start]==s[start+1])
                else:
                    isPalindrome[start].append(isPalindrome[start+1][length-2] and s[start]==s[start+length])
                    
        minCut = []
        for i in range(0, len(s)):
            if isPalindrome[0][i]:
                minCut.append(0)
            else:
                minCut.append(minCut[i-1]+1)
            for j in range(0,i):
                if isPalindrome[j+1][i-j-1]:
                    minCut[i] = min(minCut[j]+1,minCut[i])
        return minCut[len(s)-1]
