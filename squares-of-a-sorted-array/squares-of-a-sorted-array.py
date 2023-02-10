class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # A trivial solution with the built-in method sort().
        """
        for i in range(len(nums)):
        nums[i] = nums[i]**2
        nums.sort()
        return(nums)
        """
        # An another solution with two pointers to vertices of an imagined porabola.
        # [-4,-1,0,3,10]
        l = 0                               
        r = len(nums) - 1                   
        ret = [None for _ in nums]          # A dummy array for the return() function.
        l_ret = 0                           # A pointer to the ret array index.
        while l <= r:
            # The conditions fills the 'ret' array
            if abs(nums[l]) < abs(nums[r]):
                ret[l_ret] = nums[r]**2
                r -= 1
            else:
                ret[l_ret] = nums[l]**2
                l += 1
            # Move the pointer to the next ret's element
            l_ret += 1
        # Return the 'ret' array in reversed order.
        return(ret[::-1])
                
            