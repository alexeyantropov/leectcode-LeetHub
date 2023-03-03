class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [0,0,1,1,0,1,1,1]
        # The first sol, with counters.
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
        """
        # The second one, with two pointes technique
        slow, fast = 0, 0
        ret = 0
        while fast < len(nums):
            if nums[fast] == 1:
                fast += 1
            else:
                fast += 1
                slow = fast
            ret = max(ret, fast - slow)
        return(ret)