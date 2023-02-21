class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # The naive sol with the standat library.
        """
        tmp = int(''.join([str(x) for x in digits])) + 1
        return([int(x) for x in str(tmp)])
        """
        # True way with iterate through the list with extra space
        tmp = 0
        ret = []
        for i in range(len(digits)):
            if i == 0:
                s = digits[-1-i] + 1 + tmp
            else:
                s = digits[-1-i] + tmp
            tmp = s // 10
            ret.append(s%10)
        if tmp > 0:
            ret.append(1)
        return(ret[::-1])