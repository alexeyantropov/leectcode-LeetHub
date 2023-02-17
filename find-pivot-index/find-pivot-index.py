class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        sum_left = 0
        sum_right = sum(nums)
        # The first. It needs extra conditions.
        for i in range(0,len(nums)):
            if i > 0:
                sum_left += nums[i-1]
            if not i == len(nums):
                sum_right -= nums[i]
            if sum_left == sum_right:
                return(i)
        return(-1)
        """
        # The second. It's better.
        sum_left = 0
        sum_right = sum(nums)
        for i in range(len(nums)):
            sum_right -= nums[i]
            if sum_left == sum_right:
                return(i)
            sum_left += nums[i]
        return(-1)