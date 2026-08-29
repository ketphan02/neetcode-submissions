class Node:
    def __init__(self, k, v, prev=None, next=None):
        self.k = k
        self.v = v
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head
        self.capacity = capacity
        self.size = 0
        self.nodes = {}
    
    def _size(self):
        return len(self.nodes)

    def _remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

        del self.nodes[node.k]
    
    def _appendleft(self, node):
        next, prev = self.head.next, self.head
        node.next, node.prev = next, prev
        next.prev = prev.next = node

        self.nodes[node.k] = node
    
    def _pop(self):
        self._remove(self.tail.prev)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        
        node = self.nodes[key]
        self._remove(node)
        self._appendleft(node)
        return node.v
        

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            self._remove(node)
            self._appendleft(node)
            node.v = value
        else:
            while self._size() >= self.capacity:
                self._pop()
            self._appendleft(Node(key, value))
        
