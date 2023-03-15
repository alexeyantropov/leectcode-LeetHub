class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # A naive way there. It has O(N^2) complexity because of a nested loop.
        """
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return([i,j])
        """
        # A true way, with a dict for saving results from past steps to get O(N) complexity.
        memo = dict()
        for i in range(len(nums)):
            if nums[i] in memo:
                return([memo[nums[i]], i])
            else:
                memo[target - nums[i]] = i
            