# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Is there a better solution than compare nodes to each other?
        # My first needs O(N*M) times :(
        """"
        ptrA = headA
        while ptrA:
            ptrB = headB
            while ptrB:
                #print('ptrA: {}\nptrB: {}\n'.format(ptrA, ptrB))
                if ptrA == ptrB:
                    return(ptrA)
                else:
                    ptrB = ptrB.next
            ptrA = ptrA.next       
        return(None)
        """
        # The second. Is a concatenation. We can concat 'A' + 'B' and 'B' + 'A' to get the same length of the lists. Next we can iterate O(N+M) - o(N+M) iteration to get a intersection.
        ptrA, ptrB = headA, headB
        while ptrA and ptrB:
            # We get it!
            if ptrA == ptrB:
                return(ptrA)
            # The lists A+B and B+A are ender together w/o intersection
            if ptrA.next == None and ptrB.next == None:
                return(None)
            # Append B to A or still going through A
            if ptrA.next == None:
                ptrA = headB
            else:
                ptrA = ptrA.next
            # Append A to B ...
            if ptrB.next == None:
                ptrB = headA
            else:
                ptrB = ptrB.next
        return(None)