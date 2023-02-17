class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        # The simpest way is len(str)) instead of dividing (//) by 10
        ret = 0
        for i in range(len(nums)):
            tmp = nums[i]
            counter = 0
            while (tmp):
                tmp = tmp//10
                counter += 1
            if counter % 2 == 0:
                ret += 1
        return(ret)
        """
        # The second way. Convert int() to str() and count the len.
        ret = 0
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                ret += 1
        return(ret)