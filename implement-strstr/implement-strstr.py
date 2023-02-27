class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # The first solution. Built-in operators.
        if needle in haystack:
            return(haystack.index(needle))
        else:
            return(-1)