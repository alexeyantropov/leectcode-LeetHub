class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # The solution follows to the topic 'Hash table'.
        helper = dict()
        for i in range(len(nums)):
            if nums[i] in helper:
                helper[nums[i]] += 1
            else:
                helper[nums[i]] = 1
        for i in helper.keys():
            if helper[i] == 1:
                return(i)