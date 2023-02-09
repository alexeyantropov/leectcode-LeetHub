class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = heights[:] # Or copy() in py3
        expected.sort() # The built-in sort() method is really fast. 
        ret = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                ret += 1
        return(ret)