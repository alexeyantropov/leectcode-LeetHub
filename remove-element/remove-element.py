class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # nums = [0,1,2,2,3,0,4,2], val = 2
        # The first version with a built-in method 'remove'.
        # It could be O(n^2) in worse case, because 'remove' needs to check all values of a list.
        """
        for i in range(len(nums)):
            try:
                nums.remove(val)
            except:
                break
        return(len(nums))
        """
        """
        # The Second solution w/o built-in 'remove' but with the 'pop' method.
        # Just little faster than 'remove'.
        i=0
        while i < len(nums):
            if nums[i] == val:                  # If a var 'val' is found
                for j in range(i, len(nums)-1): # the loop moves all elements one position to the left
                    nums[j] = nums[j+1]
                nums.pop()                      # and reduces the list 'nums' lengt.
                continue                        
            i += 1
        return(len(nums))
        """
        # The third solution with the Two Pointers method. It needs only O(N) operations.
        # nums = [0,1,2,2,3,0,4,2]
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
        return(l)