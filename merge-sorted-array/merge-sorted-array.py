class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # The first loop compares the elements form the lists when M and N are both > 0.
        while m and n:
            print('the first loop, m: {}, n: {}'.format(m, n))
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1 
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        # The second loop fills the gaps using an existing part if the remaining list.
        while m or n:
            print('the second loop, m: {}, n: {}'.format(m, n))
            if m == 0:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            elif n == 0:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                break        
        return(nums1)