class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_ = str(x)                 # Make the the list iterable.
        if len(str(x)) < 2:
            return(True)
        for i in range(0, len(x_)):
            if i >= len(x_)//2:
                return(True)        # We have checked a half of the list and there is no reason to go further. The solution is there!
            if x_[i] == x_[-1-i]:
                continue            # The left and the right elements checked. On next step it will move pointers to a next left and righ elements.
            else:
                return(False)