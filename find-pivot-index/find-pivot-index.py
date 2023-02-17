class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [1,7,3,6,5,6]
        #  ^        sum_left=0, sum_right=sum(nums)
        #    ^      0+1,        sum(nums) - 7
        #      ^    0+1+7,      sum(nums) - 7 - 6
        sum_left = 0
        sum_right = sum(nums)
        for i in range(0,len(nums)):
            if i > 0:
                sum_left += nums[i-1]
            if not i == len(nums):
                sum_right -= nums[i]
            if sum_left == sum_right:
                return(i)
        return(-1)