class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Could it be faster than O(2N)?
        max_index = -1
        max_value = -1
        for i in range(len(nums)):
            if nums[i] > max_value:
                max_value = nums[i]
                max_index  = i
        for i in range(len(nums)):
            if nums[i] * 2 > max_value and i != max_index:
                return(-1)
        return(max_index)