class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = [0,1,1,1,2,2,3,3,4]
        """
        # The first solution with built-in list methods
        i = 0
        while i < len(nums):        # The 'while True' loop is suitable.
            if i == len(nums) - 1:
                break
            if nums[i] == nums[i+1]:
                nums.pop(i)
                continue
            i += 1
        return(len(nums))
        """
        # The second. Using of Two Pointers method. The 'l' pointer points to the last element of result list. And the 'r' point points to a considered element of the source list.
        l = 0
        r = 0
        while r < len(nums):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
            r += 1
        return(l+1)
                
                
            