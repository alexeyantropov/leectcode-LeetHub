class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        directory = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        mods = {
            'I': ['V', 'X'],
            'X': ['L', 'C'],
            'C': ['D', 'M']
        }
        
        ret = 0
        
        for i in range(len(s)):
            # The next condition works only for this task and doesn't work with digits like 'VI' or 'XI'.
            if i < len(s) - 1 and s[i] in mods and s[i+1] in mods[s[i]]:
                ret = ret - directory[s[i]]
            else:
                ret = ret + directory[s[i]]
        
        return(ret)