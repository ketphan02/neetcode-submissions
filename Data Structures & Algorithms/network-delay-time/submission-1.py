from collections import deque

class Edge:
    def __init__(self, node_id: int, time: int):
        self.node_id = node_id
        self.time = time

class Node:
    def __init__(self, node):
        self.node = node
        self.edges = []
        self.min_time = None

    def __lt__(self, other):
        return self.node < other.node

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodes = [Node(i) for i in range(n + 1)]

        for time in times:
            ui, vi, ti = time
            nodes[ui].edges.append(Edge(vi, ti))

        h = [(0, nodes[k])]
        visited = set()
        while h:
            cur_time, top = heapq.heappop(h)
            if top.node in visited:
                continue
            visited.add(top.node)
            top.min_time = cur_time
            for edge in top.edges:
                heapq.heappush(h, (cur_time + edge.time, nodes[edge.node_id]))

        res = float('-inf')
        for idx in range(1, len(nodes)):
            node = nodes[idx]
            if node is None or node.min_time is None:
                return -1
            res = max(res, node.min_time)
        
        return res