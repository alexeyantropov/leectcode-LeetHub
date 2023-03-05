class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # The first solution, up to O(N^2) complexity because of a nested loop.
        """
        ret = 10**9 + 1
        start = 0
        while start < len(nums):
            end = start
            target_ = 0
            while end < len(nums):
                target_ += nums[end]
                if target_ >= target:
                    ret = min(end - start + 1, ret)
                    break
                end += 1
            start += 1
            if ret == 1: break
        if ret == 10**9 + 1: ret = 0
        return(ret)
        """
        # The second. The sliding window approach.
        # A nested loop pulls up the 'left' pointer to the 'right' one. There is a window! And the window size is limited by sum of elements that are contained in. 
        ret = 10**9 + 1
        target_ = 0
        left, right = 0, 0
        while right < len(nums):
            target_ += nums[right]
            while target_ >= target:                # The windows size.
                ret = min(ret, right - left + 1)    # A possible result.
                target_ = target_ - nums[left]
                left += 1                           # The 'left' pointer pull up.
            right += 1
        if ret == 10**9 + 1: ret = 0
        return(ret)