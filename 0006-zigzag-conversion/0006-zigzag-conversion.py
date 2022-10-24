class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # My solution is drawing a real Zigzag and storing it in a matrix. After - just print the result from the matrix.
        
        # Initiating the matrix = O(n*m), where n = len(s), m = numRows, with a really fast code;
        # Filling the matrix = O(n), just one loop, here is a "huge" code;
        # Drawing a result string = O(n*m), a code inside loop is fast too.
        # Totally linear logic in general.

        # Init the empy matrix
        ret = []
        for i in range(numRows):
            ret.append([])
            for j in range(len(s)):
                ret[i].append(None)        
        is_going_down = False # A direction pointer that points to the direction of the zigzag (down or up-right).
        row = 0
        col = 0
        set
        # The main loop. It fills the matrix.
        for i in range(len(s)):
            print('row: {}, col: {}'.format(row, col))
            ret[row][col] = s[i]
            # An edge case.
            if numRows == 1:
                col += 1
                continue
            # When the pointer on the angle of the zigzag we should change the direction to draw new part of the figure.
            if (row + 1) % numRows == 0 or row == 0:
                is_going_down = not is_going_down
            # Move the pointer to follow the direction (down or up).   
            if is_going_down:
                row += 1
            else:
                row -= 1
                col += 2
        # Just draw the answer.
        ret_ = str()
        for i in range(len(ret)):
            for j in range(len(ret[i])):
                if ret[i][j]:
                    ret_ = ret_ + ret[i][j]
        return(ret_)