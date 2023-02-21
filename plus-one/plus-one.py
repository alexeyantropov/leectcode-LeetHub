class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # The naive sol with the standat library.
        tmp = int(''.join([str(x) for x in digits])) + 1
        return([int(x) for x in str(tmp)])