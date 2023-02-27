class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        # A simple solution, it just follows the Hint #1.
        # It needs extra memory only for storing the answer.
        """
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
        """
        # A next try. A main loop will remove elements that it will return.
        # Note: the source matrix will be changed after the main loop!
        ret = []
        while len(matrix) > 0:
            ret = ret + matrix.pop(0)
            if len(matrix) == 0 or len(matrix[0]) == 0 : break
            ret = ret + [x.pop() for x in matrix]
            if len(matrix) == 0: break
            ret = ret + matrix.pop()[::-1]
            if len(matrix) == 0 or len(matrix[0]) == 0: break
            ret = ret + [x.pop(0) for x in matrix][::-1]
        return(ret)
                    