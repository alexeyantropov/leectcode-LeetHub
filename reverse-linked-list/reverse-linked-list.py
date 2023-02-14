# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # The idea in the explanation (https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1204/) is quite different than the most popular solution. In the solution we essentially build a new L-list from the nodes and don't move a fist element step by step to the end. 
        # 1 2 3 4 5 -> 1, 2 3 4 5 -> 2 1, 3 4 5 -> 3 2 1, 4 5 -> ...
        ptr_prev = None
        ptr_tmp = None
        ptr_cur = head
        i = 0
        while ptr_cur:
            ptr_tmp = ptr_cur.next      # 2, 3, 4, 5 -> 3, 4, 5    -> 4, 5
            ptr_cur.next = ptr_prev     # 1, None    -> 2, 1, None -> 3, 2, 1, None
            ptr_prev = ptr_cur          # 1          -> 2          -> 3
            ptr_cur = ptr_tmp           # 2, 3, 4, 5 -> 3, 4, 5   -> ...
        return(ptr_prev)