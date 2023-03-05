class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # The edge cases.
        if rowIndex < 2:
            return([1] * (rowIndex+1)) # [1] or [1,1]
        # Each line is built in plaсe.
        # The first step is adding an extra element after '1',
        # All other steps are just replacing each element by its sum with a next one.
        # Totally like one the picture on top.
        ret = [1,1]
        for i in range(1, rowIndex):
            j = 1
            while j <= i:
                if j == 1:
                    ret.insert(j, ret[j-1] + ret[j])    # An extra element is added on each next row.
                else:
                    ret[j] = ret[j] + ret[j+1]          # The all next elements are sum of themselves.
                j += 1
        return(ret)
                
        