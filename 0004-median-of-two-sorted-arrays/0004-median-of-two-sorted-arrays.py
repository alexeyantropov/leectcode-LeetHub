class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_list = sorted(nums1 + nums2)
        if len(merged_list)%2: # True if it has a modulo after division -> the list has a middle element.
            median = merged_list[len(merged_list)//2]
        else:
            median = (merged_list[len(merged_list)//2] + merged_list[len(merged_list)//2 - 1]) / 2.0
        return(median)