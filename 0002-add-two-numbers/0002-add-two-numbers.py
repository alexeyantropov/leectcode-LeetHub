# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode('a head', None)
        ptr = head
        memo = 0
        while l1 or l2 or memo:
            if l1:
                l1_value = l1.val
                l1 = l1.next        # Move a pointer of the first linked list.
            else:
                l1_value = 0
                
            if l2:
                l2_value = l2.val
                l2 = l2.next        # Move a second pointer.
            else:
                l2_value = 0
            
            # The next code will fix with '//' and '%' operators!!
            new_node_val = l1_value + l2_value + memo
            if new_node_val > 9:
                memo = 1
                new_node_val = new_node_val % 10
            else:
                memo = 0
            
            new_node = ListNode(new_node_val)
            ptr.next = new_node
            ptr = new_node
            
        return(head.next)           # It returns the output list w/o firs dummy-head node.
            