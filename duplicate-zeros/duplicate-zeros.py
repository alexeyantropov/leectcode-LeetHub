class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr) - 1:
            if arr[i] == 0:
                j = len(arr)-1
                while j > i:
                    arr[j] = arr[j-1]
                    j -= 1
                arr[i+1] = 0
                i += 1
            i += 1
        return(arr)