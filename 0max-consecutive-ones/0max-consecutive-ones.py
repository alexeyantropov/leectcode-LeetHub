class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = 0
        ret = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                tmp += 1
            ret = max(ret, tmp)
            if nums[i] == 0:
                tmp = 0
        return(ret)