class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # The first way, maximum built-in functions. What could be better?
        return(' '.join(s.split()[::-1]))
        