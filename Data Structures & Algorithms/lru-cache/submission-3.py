class Node:
    def __init__(self,key=None,val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.table = defaultdict(Node)
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0
        self.capacity = capacity

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.length-=1

    def append(self,node):
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node
        self.length+=1

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        else:
            node = self.table[key]
            self.remove(node)
            self.append(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.table:
            node = Node(key=key,val = value)
            self.append(node)
            self.table[key] = node
            if self.length>self.capacity:
               lru = self.head.next
               self.remove(lru)
               del self.table[lru.key]
               del lru
        else:
            node = self.table[key]
            node.val = value
            self.remove(node)
            self.append(node)
