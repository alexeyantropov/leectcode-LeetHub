class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # This solution is based on the 'Design the Key' article.
        # Each word in the 'strs' list can mapped only in one key, because the key is the sorted word.
        # {'ant': ['tan', 'nat'], 'aet': ['eat', 'tea', 'ate']}
        memo = dict() # A dict of lists.
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key in memo:
                memo[key].append(strs[i])
            else:
                memo[key] = [strs[i]]
        # It's better to use a generator instead of a temporary variable which fills by auxiliary loop.
        return([memo[x] for x in memo])
        # Time: O(N) + a little for the generator, extra space: O(N).