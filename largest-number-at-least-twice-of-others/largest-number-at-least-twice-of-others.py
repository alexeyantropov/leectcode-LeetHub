class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Could it be faster than O(2N)?
        """
        max_index = -1
        max_value = -1
        for i in range(len(nums)):
            if nums[i] > max_value:
                max_value, max_index = nums[i], i
        for i in range(len(nums)):
            if nums[i] * 2 > max_value and i != max_index:
                return(-1)
        return(max_index)
        """
        # Could! It needs O(N).
        max_index = -1
        max_value = -1
        max_value_prev = -1
        for i in range(len(nums)):
            if nums[i] > max_value:
                max_value, max_value_prev, max_index = nums[i], max_value, i
            elif nums[i] > max_value_prev:
                max_value_prev = nums[i]
        if max_value_prev * 2 > max_value:
            return(-1)
        return(max_index)