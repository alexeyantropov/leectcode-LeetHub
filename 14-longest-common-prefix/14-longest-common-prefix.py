class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 2:
            return(''.join(strs))
        # A simplest way w/o the binary search or the bisection method.
        tmp = strs[0]
        for i in range(1, len(strs)):
            matched_letters_count = 0
            for j in range(0, min(len(tmp), len(strs[i]))):
                if tmp[j] == strs[i][j]:
                    matched_letters_count += 1
                else:
                    break                           # Stop the nested cycle to avoid incrementing the counter by next steps, example: ["CiR","CaR"]
            tmp = tmp[0:matched_letters_count]      # ["flower_etc", flower","flow","flight"] -> flower -> flow -> fl
        return(''.join(tmp))