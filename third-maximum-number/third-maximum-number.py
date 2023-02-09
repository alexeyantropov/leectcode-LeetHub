class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # The first solution. Built-in functions.
        # [2,2,3,1] -> {2,3,1} -> [2,3,1] -> [1,2,3]
        nums_ = list(set(nums))
        nums_.sort()
        if len(nums_) > 2:
            return(nums_[-3])
        else:
            return(nums_[-1])