class MyHashSet(object):

    # The first (fast) solution. It needs O(max key value) memory because of internal storage for data. Better solution is linked lists I would like to do it later.     
    def __init__(self):
        max_key = 10**6 + 1
        self.storage = [False]*max_key
        
    def add(self, key):
        self.storage[key] = True

    def remove(self, key):
        self.storage[key] = False
        
    def contains(self, key):
        return(self.storage[key])
