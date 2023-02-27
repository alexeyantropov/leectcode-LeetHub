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
        i, j, ret = 0, 0, -1
        while i < len(haystack):
            if needle[j] == haystack[i]:
                if ret == -1:            # The index init.
                    ret = i
                if j == len(needle) - 1: # If the end of the 'needle' sting is reached - there is an answer.
                    return(ret)
                i += 1
                j += 1
            elif ret == -1:              # Move on to the next element of the 'haystack' str. 
                i += 1
            else:                        # Pointers reset.
                i = ret + 1
                j = 0
                ret = -1
        return(-1)
                