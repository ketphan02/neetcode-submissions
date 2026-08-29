class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.hash_map = {}
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1

        node = self.hash_map[key]
        # Remove the node from the current idx
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        # Add to the front of the cache
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next.prev = node
    
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            # Remove the node from the current idx
            prev, next = node.prev, node.next
            prev.next = next
            next.prev = prev
            # Add to the front of the cache
            node.next = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next.prev = node
            # Update value
            node.value = value
        else:
            node = Node(key, value)
            if self.size == self.capacity:
                # remove least freq used
                real_tail = self.tail.prev
                prev, next = real_tail.prev, real_tail.next
                prev.next, next.prev = next, prev
                # delete the hash record
                del self.hash_map[real_tail.key]
                self.size -= 1

            # add a new hash record
            self.hash_map[key] = node
            # Add to the front of the cache
            node.next = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next.prev = node
            self.size += 1