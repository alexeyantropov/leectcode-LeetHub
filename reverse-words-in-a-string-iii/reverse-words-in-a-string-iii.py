class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # The first solution there are built-in methods.
        """
        return(' '.join([x[::-1] for x in s.split()]))
        """
        # The second one. Pointers are in the game.
        # Let the 's' string size is a constant!
        # In the other way we could add an extra space in the end of the string to make an edge condition for the last symbol easier.
        l, r, ret = 0, 0, str()
        while r < len(s):
            if s[r] == ' ' or r == len(s) - 1:
                if r == len(s) - 1: # there is the edge condition for a last string.
                    r_ = r
                else:
                    r_ = r - 1
                l_ = l
                if len(ret) > 0:   
                    ret = ret + ' '
                while l_ <= r_:
                    ret = ret + s[r_]
                    r_ -= 1
                r += 1; l = r
            else:
                r += 1
        return(ret)