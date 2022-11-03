class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # There's the maximum brute force solution and it works only for the problem Description.
        helper = {
            1:      'I',
            4:      'IV',
            5:      'V',
            9:      'IX',
            10:     'X',
            40:     'XL',
            50:     'L',
            90:     'XC',
            100:    'C',
            400:    'CD',
            500:    'D',
            900:    'CM',
            1000:   'M'
        }
        # A tmp variable for accumulate the return value.
        ret = str()
        for n in reversed(sorted(helper.keys())):
            # Step by step reducing the 'num' variable: 3222 -> 2222 -> 1222 -> 222 -> 122 -> 22.
            while num >= n:
                ret = ret + helper[n]
                num -= n
        return(ret)