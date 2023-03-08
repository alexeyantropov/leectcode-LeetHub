class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # The first solution there are built-in methods.
        return(' '.join([x[::-1] for x in s.split()]))