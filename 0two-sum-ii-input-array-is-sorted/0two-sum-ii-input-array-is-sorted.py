class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # It doesn't need an extra dict like the classicla Two Sum problem.
        # Because the list is sorted it helps to move pointers depending on a sum of the numbers. 
        l, r = 0, len(numbers)-1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return([l + 1, r + 1])
            elif sum < target:
                l += 1
            else: # sum > target
                r -= 1
        return([0,0])
            
        
        