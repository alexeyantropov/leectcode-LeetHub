class MyHashMap(object):

    # The simplest idea with an a list for low-level storage.
    # Needs O(max key) memory and works with O(1) complexity for standard methods.
    
    def __init__(self):
        self.storage = [None] * (10**6 + 1)
        
    def put(self, key, value):
        self.storage[key] = value
        
    def get(self, key):
        if self.storage[key] == None:
            return(-1)
        else:
            return(self.storage[key])
        
    def remove(self, key):
        self.storage[key] = None        