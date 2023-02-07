class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # The first solution. It runs on the hill and checks the top is passed or not.
        # It always consumes O(N) time.
        """
        is_upward = None
        for i in range(len(arr) - 1):
            if arr[i] < arr[i+1] and is_upward == None:
                is_upward = True
                continue
            if arr[i] < arr[i+1] and is_upward:
                continue                
            if arr[i] > arr[i+1] and is_upward:
                is_upward = False
                continue
            if arr[i] > arr[i+1] and is_upward == False:
                continue
            return(False)
        return(len(arr) > 2 and is_upward == False)
        """
        # The second. A try to use two pointers.
        # It consumes about O(N/2) time and in-loop conditions are easier.
        l = 0
        r = len(arr) - 1
        if len(arr) < 3:
            return(False)
        while l < r:
            l_moved = False
            r_moved = False
            if arr[l] < arr[l+1]:
                l_moved = True
                l += 1
            if arr[r] < arr[r-1]:
                r -= 1
                l_moved = True
            if l_moved or r_moved:
                continue
            else:
                return(False)
        return(l == r and l != 0 and r != len(arr)-1)