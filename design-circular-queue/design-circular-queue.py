# There is my complete solution.
# A list is used as a backend storage for a ring buffer of the queue.
# Initial pointers values are set as 0 and this corner case is checked in the 'enQueue' method.
# Also it's possible to set them as None or 1 like in the "Circular Queue" article.
# Extra print() calls are provided for more clear debug and understanding what is happeing. 

class MyCircularQueue(object):

    def __init__(self, k):
        self.buff = [None] * k
        self.head, self.tail = 0, 0

    def enQueue(self, value):
        if self.isFull():
            return(False)
        if self.buff[self.tail] != None:
            self.tail = (self.tail + 1) % len(self.buff)
        self.buff[self.tail] = value            
        return(True)

    def deQueue(self):
        if self.isEmpty():
            return(False)
        self.buff[self.head] = None
        if self.head != self.tail:
            self.head = (self.head + 1) % len(self.buff)
        return(True)
        
    def Front(self):
        #print('Front, buff: {}'.format(self.buff))
        if self.isEmpty():
            return(-1)
        else:
            return(self.buff[self.head])

    def Rear(self):
        #print('Rear, buff: {}, tail: {}'.format(self.buff, self.tail))
        if self.isEmpty():
            return(-1)
        else:
            return(self.buff[self.tail])
        
    def isEmpty(self):
        #print('isEmpty, head: {}, tail: {}, buff: {}'.format(self.head, self.tail, self.buff))
        if self.head == self.tail and self.buff[self.head] == None:
            return(True)
        else:
            return(False)

    def isFull(self):
        #print('isFull, buff: {}, head: {}, tail: {}'.format(self.buff, self.head, self.tail))
        if self.tail == self.head and len(self.buff) == 1 and self.buff[self.tail] != None:
            print('isFull, F 0')
            return(True)       
        if self.tail == self.head:
            print('isFull, F')
            return(False)
        if self.head < self.tail and self.tail - self.head < len(self.buff) - 1:
            print('isFull, F')
            return(False)
        if self.tail < self.head and self.head - self.tail > 1:
            print('isFull, F')
            return(False)
        #print('isFull, T')
        return(True)