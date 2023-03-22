class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        # The simplest solution.
        # It isn't important to check the Js in the S or the Ss in the J,
        # time coplexity is always will be O(len(jewels) * len(stones)).
        # But there is a little hack (because the Js are unique)
        # to reduce O(N) loopkups into the 'J' list and get O(len(stones)) time complexity.
        jewels_ = set(jewels)
        ret = 0
        for s in stones:
            if s in jewels_:
                ret += 1
        return(ret)