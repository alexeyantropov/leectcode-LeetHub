class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        # A simple solution, it just follows the Hint #1.
        x_start = 0
        y_start = 0
        x_max = n-1
        y_max = m-1
        ret = []
        while x_start <= x_max and y_start <= y_max:
            for i in range(x_start, x_max+1):
                ret.append(matrix[y_start][i])
            y_start += 1
            for j in range(y_start, y_max+1):
                ret.append(matrix[j][x_max])
            x_max -= 1
            for i in range(x_max, x_start-1, -1):
                ret.append(matrix[y_max][i])
            y_max -= 1
            for j in range(y_max, y_start-1, -1):
                ret.append(matrix[j][x_start])
            x_start += 1
        # A cheet code for fixing doubles in the 'ret' list for non-squared matrixes.
        return(ret[:m*n])
        
                    