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
        """
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
        """
        # And the last one. It uses built-in methods (and hides the loops)
        # O(4N)
        max_value = max(nums)               # O(N), scans all list.
        max_index = nums.index(max_value)   # One more O(N) to get a key by a value.
        nums.pop(max_index)                 # Needs O(N) to rebuild the list.
        max_value_prev = max(nums)          # O(N), scans all list.
        if max_value_prev * 2 > max_value:
            return(-1)
        return(max_index)