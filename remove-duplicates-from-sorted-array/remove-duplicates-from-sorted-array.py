class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = [0,0,1,1,1,2,2,3,3,4]
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
        # The second. I could rewrire pop() method like in the "Remove Element" (shifting array elements to left step by step) but why. Using the pop() method provides more clear and readable code.