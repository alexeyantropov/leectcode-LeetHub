class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        helper = dict()
        for i in range(len(nums)):
            if nums[i] in helper:
                return(True)
            else:
                helper[nums[i]] = True
        return(False)
                