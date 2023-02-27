class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # The first solution. Doesn't need any knowledge about loops and strings.
        ret = int(a,2) + int(b,2)
        return('{0:b}'.format(ret))
