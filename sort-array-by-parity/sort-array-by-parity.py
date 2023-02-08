class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # [3,1,2,4] -> [2,4,3,1]
        # [6,3,5,2,1,4] -> [6,2,4,3,5,1]
        # One more the Two Pointers example.
        # The 'l' pointer points to an odd element to be swapped,
        # the 'r' pointer searches a possible even element for swapping with odd.
        l = 0
        r = 0
        while r < len(nums):
            if nums[r] % 2 == 1:
                r += 1
            else:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
                r += 1
        return(nums)