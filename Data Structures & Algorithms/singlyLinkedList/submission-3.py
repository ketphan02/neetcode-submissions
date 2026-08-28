class Node:
    def __init__(self, v, next = None):
        self.v = v
        self.next = next

    def __str__(self):
        return f"(value: {self.v} - next: {self.next})"

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    # O(N)
    def get(self, index: int) -> int:
        if index < 0:
            return -1
        
        cnt = 0
        cur = self.head
        while cnt <= index:
            cur = cur.next
            cnt += 1
            if cur is None:
                return -1
        return cur.v
            

    # O(1)
    def insertHead(self, val: int) -> None:
        node = Node(val, self.head.next)
        if node.next is None:
            self.tail = node
        self.head.next = node

    # O(N)
    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    # O(1)
    def remove(self, index: int) -> bool:
        cnt = 0
        cur = self.head

        while cur is not None and cnt < index:
            cur = cur.next
            cnt += 1

        if cur is None or cur.next is None:
            return False

        if cur.next == self.tail:
            self.tail = cur


        cur.next = cur.next.next
        return True


    # O(N)
    def getValues(self) -> List[int]:
        res = []
        cur = self.head

        while cur:
            res.append(cur.v)
            cur = cur.next
        
        return res[1:]
