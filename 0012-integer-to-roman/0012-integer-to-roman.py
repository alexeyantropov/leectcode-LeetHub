class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
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
        ret = str()
        for n in reversed(sorted(helper.keys())):
            print('a step: n: {}, num: {}, ret: {}'.format(n, num, ret))
            while num >= n:
                ret = ret + helper[n]
                num -= n
        return(ret)