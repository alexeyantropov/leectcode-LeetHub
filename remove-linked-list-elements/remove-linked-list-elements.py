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
        # head  = [1,2,6,3,4,5,6], val = 6 -> [1,2,3,4,5]
        # head2 = [None] -> [None,1] -> [None,1,2] -> [None,1,2,3]
        pR = head
        headNew = ListNode(None)
        pL = headNew 
        while pR:
            if pR.val == val:
                pL.next = None # It's useful for the last node of the list. 
            else:
                pL.next = pR
                pL = pL.next
            pR = pR.next
        # It returns a list starts from the new 'pL.next' node for cases like '[7,7,7], 7'.
        # For other cases, when 'head.val != val', it could return 'head'.
        return(headNew.next)