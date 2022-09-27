class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ref = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        stack = []
                
        for i in range(len(s)):
            if s[i] in ref:
                stack.append(s[i])
            elif len(stack) == 0:
                return(False)
            elif s[i] == ref[stack.pop()]:
                continue
            else:
                return(False)
            
        return(len(stack) == 0)
                
                