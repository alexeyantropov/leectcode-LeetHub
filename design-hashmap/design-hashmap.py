class MyHashMap(object):

    # The simplest idea is a list for low-level storage.
    # Needs O(max key) memory and works with O(1) complexity for standard methods.    
    # The next way is using a lot of lists (buckets) and simple hash func, it would need less amount of memory.
    
    def __init__(self):
        self.max_key = 10**6
        self.buckets = 100
        self.storage = [None] * (self.buckets + 1)
        
    def get_bucket(self, key):
        return(divmod(key, self.buckets)[::-1])
        
    def put(self, key, value):
        bucket, offset = self.get_bucket(key)
        if self.storage[bucket] == None:
            self.storage[bucket] = [None] * ((self.max_key // self.buckets) + 1)
        self.storage[bucket][offset] = value
        
    def get(self, key):
        b, o = self.get_bucket(key)
        if self.storage[b] == None:
            return(-1)
        if self.storage[b][o] == None:
            return(-1)
        else:
            return(self.storage[b][o])
        
    def remove(self, key):
        b, o = self.get_bucket(key)
        if not self.storage[b] == None:
            self.storage[b][o] = None