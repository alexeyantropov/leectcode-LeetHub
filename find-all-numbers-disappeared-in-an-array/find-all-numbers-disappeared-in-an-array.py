class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        # The naive solutions is build an empty list and fill it by elements from the 'nums' list.
        # After we could find empty elements indexes and vaules. It needs extra space for a tmp list.
        # It needs extra memory but doesn't change the 'nums' list.
        
        # The second brude-force solution is the "barley-break" method.
        # But nested loop could take some time to place each element on the plase.
        ret = []
        for i in range(len(nums)):
            # A value is out of the place. Possible it's a desired value. 
            if i != nums[i] - 1:
                index_to = nums[i] - 1
                while True:
                    nums[i], nums[index_to] = nums[index_to], nums[i]
                    index_to = nums[i] - 1
                    # The 'while' loop has reaced the goal if the vaule on the place.
                    if index_to == nums[index_to] - 1: 
                        break
            # Double check. The value on the place or no?
            # On this step we can get expected disappeared values or vaules that haven't fixed yet.
            if i != nums[i] - 1:
                ret.append(i+1)
        # Some values have been fixed, some no. Final check here. << O(n)
        ret_ = []
        for i in range(len(ret)):
            if ret[i] != nums[ret[i]-1]:
                ret_.append(ret[i])
        return(ret_)
        """
        
        # The third solution - mark/flip values that on the places by '-1'
        # It is the fastest solution.
        ret = []
        for i in range(len(nums)):
            # Mark values on all indexes that is reads from values.
            nums[abs(nums[i]) - 1] = abs(nums[abs(nums[i]) - 1]) * -1
        for i in range(len(nums)):
            # If a vaules isn't marked - the first loop didn't gen this index 'i'.
            # And expected disappeared value (or index) here!
            if abs(nums[i]) == nums[i]:
                ret.append(i+1)
        return(ret)