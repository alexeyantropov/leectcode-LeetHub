class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = {}                            # A dict as the helper 'tmp', not a list. O(1) vs. O(n) for searching entry of an element.
        ret = 0
        i = 0
        while i < len(s):
            if s[i] in tmp:
                ret = max(ret, len(tmp))
                i = tmp[s[i]] + 1           # Move the pointer 'i' to first letter after the repeaded letter.
                tmp = {}
            tmp[s[i]] = i
            i += 1
            
        return(max(ret, len(tmp)))