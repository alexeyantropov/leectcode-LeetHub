class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # The second solution. More faster.
        # Let's check all possible sub-strings witch a current element in the middle.
        
        def generate_max_polindrome(s_, l, r):
            while l >= 0 and r < len(s_):
                if s_[l] == s_[r]:
                    l -= 1
                    r += 1
                else:
                    break
            return(s_[l+1:r])
        
        memo = str()
        memo2 = str()
        ret = str()
        for i in range(len(s)):
            memo = generate_max_polindrome(s, i, i)
            # This cond for cases like 'cbbd'.
            # We should set edge pointers 'l' and 'r' like the first 'b' and the second 'b'
            # because the middile of the palindrome is between the pointers.
            # If else, we set them like the middle element of string 's_'.
            memo2 = generate_max_polindrome(s, i, i+1)
            if len(memo2) > len(ret):
                ret = memo2
            elif len(memo) > len(ret):
                ret = memo
                
        return(ret)
        
        """
        # There is a first solution. Naive and long.
        def is_palindrome(s_):
            for i in range(len(s_)//2):
                if s_[i] == s_[-1-i]:
                    continue
                else:
                    return(False)
            return(True)
        
        # A function that define a pointer that points on the begiging on disired string. 
        def reinit_vars(ptr_):
            return(ptr_ + 1, ptr_ + 1, str())
        
        ptr_start, ptr, memo = reinit_vars(-1)
        ret = str()
        
        while ptr < len(s):
            memo = memo + s[ptr]
            if is_palindrome(memo) and len(memo) > len(ret):
                ret = memo
            ptr += 1

            if ptr == len(s) and ptr_start < len(s):
                # Move a pointer of the first element righter. And check a new string w/o the first element, w/o the first and the second, w/o ... .
                ptr_start, ptr, memo = reinit_vars(ptr_start)
                
            # A good idea to skip extra checks. When the already founded desired string is bigger than all possible new strings.
            if len(s) - ptr_start < len(ret):
                break
        
        return(ret)
        """