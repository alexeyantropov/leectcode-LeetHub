class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # An idea is the brute force a digit by the "following process".
        # There are two possibilities.
        # The first possibility is the digit is a happy one (19->82->68->100),
        # the second one is the digit produces a loop (2->4->37->42->16->145->89->58->4) and the digit is'n a happy one!
        # A memo: divmod(xyz, 10) = (xy, z); divmod(xy, 10) = (x, y); divmod(x, 10) = (0, x).
        # The change of '//' and '%' operators in one function.
        memo = set()
        while n != 1 and n not in memo:
            tmp, digit = 0, n
            memo.add(n)
            while digit > 0: # the "following process" is there.
                digit, digit_ = divmod(digit, 10)
                tmp += digit_ ** 2
            n = tmp
        return(n == 1)
    