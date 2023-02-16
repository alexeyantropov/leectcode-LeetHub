# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # head = [1,2,3,4,5] -> [2,4] + [1,3,5] -> [2,4,1,3,5]
        ptr = head
        head_1 = ListNode(None)
        head_2 = ListNode(None)
        ptr_1 = head_1
        ptr_2 = head_2
        flag = True
        while ptr:
            if flag:
                ptr_1.next = ptr
                ptr_1 = ptr_1.next
            else:
                ptr_2.next = ptr
                ptr_2 = ptr_2.next
            flag = not flag
            ptr = ptr.next
        ptr_2.next = None
        ptr_1.next = head_2.next
        return(head_1.next)