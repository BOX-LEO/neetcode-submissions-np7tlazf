class Node:
    def __init__(self,key=None,val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {} #key:node
        
    def _remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _append(self,node):
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        node.next = self.tail
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._append(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._append(node)
            node.val = value
        else:
            if len(self.cache) == self.capacity:
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]
            new_node = Node(key,value)
            self.cache[key] = new_node
            self._append(new_node)