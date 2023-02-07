class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
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
        