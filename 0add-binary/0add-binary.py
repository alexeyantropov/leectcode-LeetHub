class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # The first solution. Doesn't need any knowledge about loops and strings.
        """
        ret = int(a,2) + int(b,2)
        return('{0:b}'.format(ret))
        """
        # The second.
        """
        ret = str()
        tmp = 0
        ptr_a, ptr_b = len(a) - 1, len(b) - 1
        while ptr_a >= 0 or ptr_b >= 0 or tmp > 0:
            if ptr_a >= 0:
                tmp = tmp + int(a[ptr_a])
            if ptr_b >= 0:
                tmp = tmp + int(b[ptr_b])
            if tmp == 0:
                ret = ret + '0'
            elif tmp == 1:
                ret = ret + '1'
                tmp = 0
            elif tmp == 2:
                ret = ret + '0'
                tmp = 1
            else: # tmp > 2
                ret = ret + '1'
                tmp = 1
            ptr_a -= 1
            ptr_b -= 1
        return(ret[::-1])
        """
        # The third one, more clear.
        ret, tmp, ptr_a, ptr_b = '', 0, len(a)-1, len(b)-1 
        while ptr_a >= 0 or ptr_b >= 0:
            if ptr_a >= 0:
                tmp = tmp + int(a[ptr_a])
            if ptr_b >= 0: 
                tmp = tmp + int(b[ptr_b])
            ret = ret + str(tmp % 2)
            if tmp > 1:
                tmp = 1
            else:
                tmp = 0
            ptr_a -= 1; ptr_b -= 1
        if tmp > 0:
            ret = ret + str(tmp)
        return(ret[::-1])