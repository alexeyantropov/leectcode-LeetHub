class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # The task is the same as the 'two sum'.
        # The first if-conditional checks arr[i] == 2 * arr[j], 
        # the second if-cond checks arr[i] == arr[j] // 2.
        # The second cond is necessary beacus the list is unsorted (7->14 or 14->7).
        memo = {}
        for i in range(len(arr)):
            if arr[i] * 2 in memo or (arr[i] // 2 in memo and arr[i] % 2 == 0) :
                return(True)
            else:
                memo[arr[i]] = i
        return(False)