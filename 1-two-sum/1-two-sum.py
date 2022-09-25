class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # A naive way there. It takes O(N^2) time.
        """
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return([i,j])
        """
        # A true way with extra dict for saving results of prev iterations.   
        tmp = {}
        for i in range(0, len(nums)):
            expected_value = target - nums[i] # 
            if nums[i] in tmp:
                return([tmp[nums[i]], i])
            else:
                tmp[expected_value] = i