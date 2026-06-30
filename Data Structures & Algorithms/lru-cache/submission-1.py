class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        value = self.cache.get(key, -1)
        if value != -1:
            self.cache.pop(key)
            self.cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if len(self.cache.keys()) == self.capacity:
            self.cache.popitem(last=False)    
        self.cache[key] = value
