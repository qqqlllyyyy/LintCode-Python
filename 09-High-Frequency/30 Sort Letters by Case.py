# Sort Letters by Case
# Given a string which contains only letters. Sort it by lower case
# first and upper case second.
#
# Example
# For "abAcD", a reasonable answer is "acbAD"
# Note
# It's not necessary to keep the original order of lower-case letters and
# upper case letters.
#
# Challenge
# Do it in one-pass and in-place.

class Solution:
    """
    @param chars: The letters array you should sort.
    """
    def sortLetters(self, chars):
        # write your code here
        upperSet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        start, end = 0, len(chars) - 1
        while start <= end:
            while start <= end and chars[start] not in upperSet:
                start += 1
            while start <= end and chars[end] in upperSet:
                end -= 1
            
            if start <= end:
                temp = chars[end]
                chars[end] = chars[start]
                chars[start] = temp
        return

