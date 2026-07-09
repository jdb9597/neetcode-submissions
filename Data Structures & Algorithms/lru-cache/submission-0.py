class DNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.head = DNode()
        self.tail = DNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_front(node)
        return node.val
        

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            node.val = value
        else:
            node = DNode(key,value)
            self._add_front(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                removed = self._pop_back()
                del self.cache[removed.key]

    def _add_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_front(self, node):
        self._remove(node)
        self._add_front(node)

    def _pop_back(self):
        if self.tail.prev == self.head:
            return None
        result = self.tail.prev
        self._remove(result)
        return result
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)