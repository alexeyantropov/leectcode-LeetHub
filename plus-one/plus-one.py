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
        """
        # A way with iterate through the list with extra space.
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
        """
        # What about avoid to extra space usage?
        tmp = 0
        digits = digits[::-1] # [1,2,3] -> [3,2,1]
        digits[0] = digits[0] + 1
        for i in range(len(digits)):
            digits[i] = digits[i] + tmp
            tmp = digits[i] // 10
            if tmp > 0:
                digits[i] = digits[i] % 10
        if tmp > 0:
            digits.append(1)
        return(digits[::-1])