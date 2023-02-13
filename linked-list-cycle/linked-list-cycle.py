# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def checkThemAll(self, pointer_one, pointer_two):
        if pointer_one == pointer_two:
            return(True)
        else:
            return(False)
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ptr_fast = head
        ptr_slow = head
        # Double check is necessary because the 'fast' pointer couldn't meet the 'slow' pointer. And main loop will take an extra circle.
        while ptr_fast and ptr_fast.next:
            ptr_fast = ptr_fast.next
            if self.checkThemAll(ptr_fast, ptr_slow):
                return(True)
            ptr_slow = ptr_slow.next
            ptr_fast = ptr_fast.next
            if self.checkThemAll(ptr_fast, ptr_slow):
                return(True)
        return(False)