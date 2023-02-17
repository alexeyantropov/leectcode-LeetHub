# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # The first solution: with an extra list, it needs O(N) operations to fill the list
        # and O(N/2) ops to check the palindrome pattern. 
        tmp = []
        ptr = head
        while ptr:
            tmp.append(ptr.val)
            ptr = ptr.next
        l = 0
        r = len(tmp) - 1
        while l <= r:
            if tmp[l] == tmp[r]:
                l += 1
                r -= 1
            else:
                return(False)
        return(True)