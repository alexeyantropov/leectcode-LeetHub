class MyHashMap(object):

    # The simplest idea is a list for low-level storage.
    # Needs O(max key) memory and works with O(1) complexity for standard methods.
    # If keys is alphanumeric then it will need O(2 * max key) memory for storring keys and values.
    
    # The next way is using a tree of lists, it would need less amount of memory.
    
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