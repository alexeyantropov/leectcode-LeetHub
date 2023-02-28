class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # ["flower","flow","flight"]
        if len(strs) > 1:
            prefix = strs[0] # flower
        else:
            return(strs[0])
        # On the first step it compares 'flower' with 'flow' and gets 'flow',
        # on the second it compares 'flow' with 'flight' and gets 'fl'.
        # Nested loops doesn't do extra steps when finds different letters.
        # The main loop also doesn't do extra streps if words isn't same (len(prefix)==0).
        for i in range(1, len(strs)):
            ptr = 0
            while ptr < len(prefix) and ptr < len(strs[i]):
                if prefix[ptr] == strs[i][ptr]:
                    ptr += 1
                else:
                    break
            prefix = prefix[:ptr]
            if len(prefix) == 0:
                return(prefix)
        return(prefix)