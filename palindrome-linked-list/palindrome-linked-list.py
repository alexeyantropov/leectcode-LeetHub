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
        """
        # The second. We can build a extra list whitch will contain a half of the original list.
        # Next we can compare step by step all nodes values. [1,2,3,3,2,1] -> [3,2,1] + [3,2,1]
        # Reversing like in the 'Reverse Linker List' problem.
        # [1,2,3,4,5,6] -> [1, 2,3,4,5,6] -> [2,1, 3,4,5,6] -> [3,2,1, 4,5,6]
        head_reversed = None
        ptr_tmp = None
        ptr = head
        ptr_fast = head
        # ptr is the main pointer, ptr_fast is used for the loop ending.
        while ptr and ptr_fast and ptr_fast.next: 
            ptr_fast = ptr_fast.next.next
            ptr_tmp = ptr.next
            ptr.next = head_reversed            
            head_reversed = ptr         
            ptr = ptr_tmp
        # On this line the 'head_reversed' list has a half of the 'head' list in reverse order
        # head = [1,2,3,4,5,6] (was), head_reversed = [3,2,1].
        # If len of the original 'head' list is odd then it should move the pointer ptr on next node!
        # Because 'ptr_fast' is reached the end of the 'head' list in one step earlier.
        # [1,2,3,4,5,6,7] -> ptr_reversed[1,2,3] + ptr[4,5,6,7]
        if ptr_fast:
            ptr = ptr.next
        ptr_reversed = head_reversed
        while ptr and ptr_reversed:
            if not ptr.val == ptr_reversed.val:
                return(False)
            ptr = ptr.next
            ptr_reversed = ptr_reversed.next
        return(True)