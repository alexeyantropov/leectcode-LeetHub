class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort() # It will be usefull next. For cases like [-1, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 1].

        # There is a border cond, let's skip it.
        if len(nums) == 3 and nums[0] + nums[1] + nums[2] == 0:
            return([sorted(nums)])

        # Let's turn the problem to 2sum-like.
        # The main loop makes a 'target' every step and the nested loop solves the 2sum problem for the target.
        for i in range(len(nums)):
            two_sum_helper = {}
            target = nums[i]
            for j in range(i + 1, len(nums)):
                if j > 2 and nums[j] == nums[j-1] == nums[j-2] == nums[j-3]: # The cond for a strange case.
                    continue
                expected = - 1 * (target + nums[j]) 
                if expected in two_sum_helper:
                    ret_ = sorted([target, nums[j], expected])  # It's to avoid dublicates in the answer.
                    if ret_ not in ret:
                        ret.append(ret_)
                else:
                    two_sum_helper[nums[j]] = expected # or j, or True, or smth
        return(ret)

        # Ufff! I did it!!1 After many many 'Time Limit' versions.
        # Cpu util: A little less that O(n^2) because the nested loop is always shorter on next step of the main loop.