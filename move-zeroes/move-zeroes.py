class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # nums = [0,1,0,3,12]
        # nums = [1,1,0,0,3,12]
        l = 0 # The pointer points on a zero element index for writing non-zero element from the next pointer.
        r = 0 # This pointer runs faster to the right over the 'nums' list.
        while r < len(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
