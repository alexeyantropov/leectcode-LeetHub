class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # A helper function that calculates the water amount like an area in the container. 
        def calc_area(h, left_border, right_border):
            first_side = right_border - left_border
            second_side = min(h[left_border], h[right_border])
            return(first_side * second_side)
        # Pointers to the borders of the container and the area initial value.
        l = 0
        r = len(height) - 1
        ret = 0
        # The main loop!
        while l < r:
            tmp = calc_area(height, l, r)
            if tmp > ret:
                ret = tmp
            # It moves only smaller/lower border of the container for get a chance to get bigger area on next step.
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return(ret)