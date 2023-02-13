# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # The first step. A try to find a Node inside a loop. If the Node doesn't exist then return(None).
        ptr_slow = head
        ptr_fast = head
        if not ptr_fast:
            return(None)
        while ptr_fast:
            if not (ptr_fast.next and ptr_fast.next.next):
                return(None)
            ptr_fast = ptr_fast.next.next
            ptr_slow = ptr_slow.next
            if ptr_fast == ptr_slow:
                ptr_in_loop = ptr_fast
                break
        # The second step. Running inside a loop to find an expected node.
        ptr_slow = head
        ptr_fast = head.next
        while ptr_slow:
            while ptr_fast:
                if ptr_fast == ptr_slow:
                    return(ptr_fast)
                elif ptr_fast == ptr_in_loop:
                    ptr_fast = ptr_fast.next
                    break
                else:
                    ptr_fast = ptr_fast.next
            ptr_slow = ptr_slow.next        
        return(None)