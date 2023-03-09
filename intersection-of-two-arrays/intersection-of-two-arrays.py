class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        helper = {}
        ret = []
        for i in range(len(nums1)):
            helper[nums1[i]] = True
        for i in range(len(nums2)):
            if nums2[i] in helper and helper[nums2[i]]:
                ret.append(nums2[i])
                helper[nums2[i]] = False
        return(ret)