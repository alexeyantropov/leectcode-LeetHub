class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # The first version.
        ret = [[1], [1,1]]
        if numRows == 1:
            return(ret[:1])
        elif numRows == 2:
            return(ret)
        for i in range(2, numRows):
            ret.append([1])
            for j in range(0, i-1):
                ret[-1].append(ret[-2][j] + ret[-2][j+1])
            ret[-1].append(1)
        return(ret)