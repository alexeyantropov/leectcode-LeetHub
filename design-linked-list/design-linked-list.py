# The classical Leetcode definition of a node.
class ListNode(object):
    def __init__(self, val=0, next=None):
        #print('ListNode:\n self: {},\n val: {},\n next: {}.'.format(self, val, next))
        self.val = val
        self.next = next
# Debug messages that are below via the 'print' function could help understanding what is happening with the pointers.
# The most important disadvantage of my approach is no counder of the list lenght. It leads to extra checks for a pointer value.
class MyLinkedList(object):
    def __init__(self, val=None, next=None):
        self.head = None
        #print('__init__,\n val: {},\n head: {}.'.format(val, self.head))

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        ptr = self.head
        for i in range(index):
            if not ptr:
                return(-1)
            ptr = ptr.next
            #print('get:\n index: {},\n i: {},\n ptr: {}.'.format(index, i, ptr))
        if ptr:
            return(ptr.val)
        else:
            return(-1)
        
    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val, self.head)
        self.head = new_node
        #print('addAtHead:\n head: {},\n new_node: {}.'.format(self.head, new_node))
        
    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        ptr = self.head
        if not ptr: # An edge case. Adding into emply list.
            self.addAtHead(val)
            return()
        while ptr:
            last_node = ptr
            ptr = ptr.next
        last_node.next = ListNode(val)
        #print('addAtTail:\n last_node: {},\n last_node.val: {},\n last_node.next: {}.'.format(last_node, last_node.val, last_node.next))

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0: # An edge case, prev_node doesn't exist.
            self.addAtHead(val)
            return()
        ptr = self.head
        prev_node = self.head
        for i in range(index):
            if not ptr:
                return(-1)
            prev_node = ptr
            ptr = ptr.next
        new_node = ListNode(val, ptr)
        prev_node.next = new_node
        #print('addAtIndex:\n prev_node: {},\n ptr: {},\n new_node: {}.'.format(prev_node, ptr, new_node))
        
    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        ptr = self.head
        if index == 0: # An edge case.
            self.head = ptr.next
            return()
        prev_node = self.head
        for i in range(index):
            if not ptr:
                return(-1)
            prev_node = ptr
            ptr = ptr.next
        if prev_node and ptr:
            prev_node.next = ptr.next
        else:
            return(-1)
        #print('deleteAtIndex:\n prev_node: {},\n ptr: {}'.format(prev_node, ptr))

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)