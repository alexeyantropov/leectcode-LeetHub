class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # A first way (may and the last one) is building a hash map.
        # If a key exists (1st word) then a value is known (2st word).
        # If the value doesn't match a letter from the word then return False.
        # If the key isn't exists then a new k-v pair has to be added.
        helper = dict()
        helper_ = dict() # The same in an opposite way.
        if len(s) != len(t):
            return(False)
        def deal_with_helper(h, a, b):
            if a not in h:
                h[a] = b
            elif a in h and h[a] != b:
                return(False)
            return(True)
        for i in range(len(s)):
            if deal_with_helper(helper, s[i], t[i]) and deal_with_helper(helper_, t[i], s[i]):
                continue
            else:
                return(False)
        return(True)