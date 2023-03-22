class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # The first approach. Time compexity is O(2N) and memory is O(set(N)).
        """
        helper = {}
        for char in s:
            if char in helper:
                helper[char] += 1
            else:
                helper[char] = 1
        for idx, char in enumerate(s):
            if helper[char] == 1:
                return(idx)
        return(-1)
        """
        # An another way with only one loop. And may be the first is clearer.
        memo, i, ret = dict(), 0, -1
        while i < len(s):
            # print('i: {}, s[i]: {}, ret: {}, memo: {}.'.format(i, s[i], ret, memo))
            if s[i] in memo and memo[s[i]] == ret: # Reset
                ret = -1
                i = memo[s[i]]
            elif s[i] in memo and memo[s[i]] == i and ret == -1: # Set after reset
                ret = i
            elif s[i] not in memo and ret == -1: # Set firstime
                ret = i
                memo[s[i]] = i
            elif s[i] not in memo:
                memo[s[i]] = i
            else:
                pass
            i += 1
        return(ret)