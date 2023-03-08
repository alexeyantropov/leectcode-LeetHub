class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # The first way, maximum built-in functions. What could be better?
        '''
        return(' '.join(s.split()[::-1]))
        '''
        # The second one.
        initial_size, l, r = len(s), len(s) - 1, len(s)
        while l > -1:
            if s[l] == ' ' and l == r - 1:
                l -= 1; r -= 1
                continue
            if s[l] != ' ' and l > 0:
                l -= 1
            else:
                if s[l] != ' ':
                    s = s + ' '
                s = s + s[l:r]
                l -= 1; r = l + 1
        return(s[initial_size + 1:len(s)])