# Rotate String
# Given a string and an offset, rotate string by offset.
# (rotate from left to right)
#
# Example
# Given "abcdefg".
# offset=0 => "abcdefg"
# offset=1 => "gabcdef"
# offset=2 => "fgabcde"
# offset=3 => "efgabcd"
#
# Challenge
# Rotate in-place with O(1) extra memory.

class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, s, offset):
	    # write you code here
	    if len(s) == 0: return "" # Can not use "if s == "":" here, why?
	    offset %= len(s)
	    self.reverse(s, 0, len(s) - 1)
	    self.reverse(s, 0, offset - 1)
	    self.reverse(s, offset, len(s) - 1)
	    return

    def reverse(self, s, start, end):
        while start < end:
            temp = s[end]
            s[end] = s[start]
            s[start] = temp
            start += 1
            end -= 1
        return
