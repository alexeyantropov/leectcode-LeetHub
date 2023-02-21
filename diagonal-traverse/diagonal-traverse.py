class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        n, m = len(mat), len(mat[0])
        # This function goes through a matrix like a oblique rain.
        #   /  /  /  / 
        # [1, 2, 3, 4]/
        # [5, 6 ,7, 8]/
        # [9, 0, 1, 2]
        # The first drop gets [1], the second [2,4], the third [3,6,9], next [4,7,0], [8,1] and [2] 
        def get_diagonal(x, y):
            tmp = []
            d = x + y
            while x > -1 and y < n:
                tmp.append(mat[y][x])
                x -= 1
                y += 1
            # A conditional that flips every odd result (see direction of the lines on example picture).
            if d % 2 == 0:
                tmp = tmp[::-1]
            return(tmp)
        # Could it be a single loop?
        diagonal_number = 0
        for i in range(m):
            ret = ret + get_diagonal(i, 0)
        for i in range(1,n):
            ret = ret + get_diagonal(m-1, i)
        return(ret)
                
