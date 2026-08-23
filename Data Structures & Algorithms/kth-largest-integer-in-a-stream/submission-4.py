from collections import deque

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.l = 0
        self.heap = deque()
        self.k = k
        for num in nums:
            self._add(num)

    def _add(self, val: int):
        self.heap.append(val)
        idx = len(self.heap) - 1
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if 0 <= idx < len(self.heap) and 0 <= parent_idx < len(self.heap) and self.heap[idx] > self.heap[parent_idx]:
                self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
                # print(idx, parent_idx, self.heap)
                idx = parent_idx
            else:
                break

    def _pop(self) -> int:
        res = self.heap[0]
        self.heap[0] = self.heap.pop()
        idx = 0
        while idx < len(self.heap):
            cidx_1, cidx_2 = idx * 2 + 1, idx * 2 + 2
            if cidx_1 >= len(self.heap):
                break
            if cidx_2 >= len(self.heap) and self.heap[idx] < self.heap[cidx_1]:
                self.heap[idx], self.heap[cidx_1] = self.heap[cidx_1], self.heap[idx]
                idx = cidx_1
            elif cidx_2 < len(self.heap) and self.heap[cidx_2] < self.heap[cidx_1] and self.heap[idx] < self.heap[cidx_1]:
                self.heap[idx], self.heap[cidx_1] = self.heap[cidx_1], self.heap[idx]
                idx = cidx_1
            elif cidx_2 < len(self.heap) and self.heap[cidx_2] >= self.heap[cidx_1] and self.heap[idx] < self.heap[cidx_2]:
                self.heap[idx], self.heap[cidx_2] = self.heap[cidx_2], self.heap[idx]
                idx = cidx_2
            else:
                break

        return res

    def add(self, val: int) -> int:
        self._add(val)
        add_back = []
        cnt = 0
        res = None
        while cnt < self.k - 1:
            add_back.append(self._pop())
            cnt += 1
        res = self.heap[0]
        for num in add_back:
            self._add(num)
        return res
