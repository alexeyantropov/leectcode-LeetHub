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
        """
        # head = [1,2,3,4,5] -> [2,4] + [1,3,5] -> [2,4,1,3,5]
        # Main idea is using a flag variable that changes every step.
        # This way the code can put odd and even variables to different list
        ptr = head
        head_1 = ListNode(None)
        head_2 = ListNode(None)
        ptr_1 = head_1
        ptr_2 = head_2
        # The flag.
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
        """
        # The second way w/o flag
        # The odd-numbered nodes will be connected to each other (from the first node of the 'head' list),
        # and a tmp list will be buill from the even-numbered nodes.
        # [1,2,3,4,5] + None -> [1,3,4,5] + [1] -> [1,3,5] + [1,4]
        if not head:
            return(None)
        elif not head.next:
            return(head)
        else:
            pass
        ptr = head
        head_2 = head.next
        ptr_2 = head_2
        while ptr.next and ptr_2.next:
            ptr.next = ptr_2.next
            ptr = ptr_2.next
            ptr_2.next = ptr.next
            ptr_2 = ptr_2.next
        ptr.next = head_2
        return(head)