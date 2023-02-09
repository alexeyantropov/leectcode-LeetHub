class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        # The naive solutions is build an empty list and fill it by elements from the 'nums' list.
        # After we could find empty elements indexes and vaules. It needs extra space for a tmp list.
        
        # The second solution is the "barley-break" method. But nested loop could take some time.
        ret = []
        for i in range(len(nums)):
            if i != nums[i] - 1: # A value is out of the place. Possible it's a desired value. 
                index_to = nums[i] - 1
                while True:
                    nums[i], nums[index_to] = nums[index_to], nums[i]
                    index_to = nums[i] - 1
                    if index_to == nums[index_to] - 1: # A value on the place
                        break
            if i != nums[i] - 1: # Double check. A value has been fixed or no after the game.
                ret.append(i+1)
        # Some values have been fixed, some no. Final check here. << O(n)
        ret_ = []
        for i in range(len(ret)):
            if ret[i] != nums[ret[i]-1]:
                ret_.append(ret[i])
        return(ret_)
        """
        
        # The third solution - mark values that just could be on the places,
        # this way we will find indexes w/o the marks.
        ret = []
        for i in range(len(nums)):
            print(i)
            nums[abs(nums[i]) - 1] = abs(nums[abs(nums[i]) - 1]) * -1
        for i in range(len(nums)):
            if abs(nums[i]) == nums[i]:
                ret.append(i+1)
        return(ret)