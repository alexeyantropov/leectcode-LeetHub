class Solution(object):
    def reverseString(self, s, l = None, r = None):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # The trivial solution with built-in operators.
        """
        s = s[::-1]
        """
        # The expected sol with the two-pointers technique.
        """
        l, r = 0, len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        """
        # The third sol with the recursion approach.
        # For this method I changed args of the function to avoid add an extra subfunction.
        if l == None or r == None:
            l, r = 0, len(s) - 1
        if not l < r:
            return()
        s[l], s[r] = s[r], s[l]
        self.reverseString(s, l+1, r-1)
        