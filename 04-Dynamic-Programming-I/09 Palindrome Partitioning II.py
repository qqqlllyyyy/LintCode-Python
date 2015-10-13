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
        n = len(s)
        isPalindrome = [[] for i in range(n)]
        
        for length in range(n):
            for start in range(n - length):
                if length == 0:
                    isPalindrome[start].append(True)
                elif length == 1:
                    isPalindrome[start].append(s[start] == s[start + 1])
                else:
                    isPalindrome[start].append(s[start] == s[start + length] and isPalindrome[start + 1][length - 2])
                    
        minCut = [float("infinity") for i in range(n)]
        for i in range(n):
            if isPalindrome[0][i]:
                minCut[i] = 0
            else:
                for j in range(i):
                    if isPalindrome[j + 1][i - j - 1]:
                        minCut[i] = min(minCut[i], minCut[j] + 1)
        return minCut[n - 1]
