class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # The first solution. Built-in operators.
        """
        if needle in haystack:
            return(haystack.index(needle))
        else:
            return(-1)
        """
        # The second.
        # sadbutsad
        # sad, but, nut, bud
        i, j, ret = 0, 0, -1
        while i < len(haystack):
            print(i,j)
            if needle[j] == haystack[i]:
                if ret == -1: # index init
                    ret = i
                if j == len(needle) - 1:
                    return(ret)
                i += 1
                j += 1
            elif ret == -1: 
                i += 1
            else:
                i = ret + 1
                j = 0
                ret = -1
                
        return(-1)
                