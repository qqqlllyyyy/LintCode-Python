# Simplify Path
# Given an absolute path for a file (Unix-style), simplify it.
#
# Example
# "/home/", => "/home"
# "/a/./b/../../c/", => "/c"
#
# Challenge
# 1. Did you consider the case where path = "/../"?
#    In this case, you should return "/".
# 2. Another corner case is the path might contain multiple slashes '/'
#    together, such as "/home//foo/".
#    In this case, you should ignore redundant slashes and return "/home/foo".
#
#
class Solution:
    # @param {string} path the original path
    # @return {string} the simplified path
    def simplifyPath(self, path):
        # Write your code here
        result = '/'
        
        list1 = path.split('/')
        paths = []
        
        for s in list1:
            if s == '..':
                if len(paths) > 0:
                    paths = paths[ : len(paths) - 1]
            elif s != '.' and s != '':
                paths.append(s)
        
        for s in paths:
            result += s
            result += '/'
        
        # Remove the last '/' if needed
        if len(result) > 1:
            result = result[ : len(result) - 1]
        return result
