class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        if len(nums) == 2:
            return(min(nums))
        l, r = len(nums)-2, len(nums)-1
        nums.sort()
        while r > 0: # It could be a 'for' loop by sorted(nums), if the 'nums' var is unchangeable. 
            ret = ret + min(nums[l], nums[r])
            l -= 2; r -= 2
        return(ret)