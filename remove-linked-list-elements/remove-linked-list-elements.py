# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # head = [1,2,6,3,4,5,6], val = 6 -> [1,2,3,4,5]
        # head_new = [None] -> [None,1] -> [None,1,2] -> [None, 1,2,3]
        p = head
        head_new = ListNode(None)
        p_new = head_new
        while p:
            if p.val == val:
                p_new.next = None # It's useful for the last node of the list. 
            else:
                p_new.next = p
                p_new = p_new.next
            p = p.next            
        return(head_new.next)