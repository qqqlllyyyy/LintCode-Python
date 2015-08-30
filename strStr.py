# strStr
# strstr (a.k.a find sub string), is a useful function in string operation.
# Your task is to implement this function.
# For a given source string and a target string,
# you should output the first index(from 0) of target string in source string.
# If target does not exist in source, just return -1.
#
# Example
# If source = "source" and target = "target", return -1.
# If source = "abcdabcdefg" and target = "bcd", return 1.


class Solution:
    def strStr(self, source, target):

        # 'None' is the notation for Null in Python
        if (source == None) or (target == None) or (len(source) < len(target)):
            return -1;
            
        i = 0;
        while i < len(source) - len(target) + 1:
            j = 0; k = i;
            while j < len(target):
                if target[j] == source[k]:
                    j += 1; k += 1;
                else:
                    break;
            if j == len(target): # Don't forget this step. We can return i only if we have looped through all characters in target. 
                return i;
            i += 1;
        return -1;
