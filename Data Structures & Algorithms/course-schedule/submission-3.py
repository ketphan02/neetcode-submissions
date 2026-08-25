class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0 for _ in range(numCourses)]
        adj = defaultdict(list)

        for u,v in prerequisites:
            adj[u].append(v)
            in_degree[v] += 1

        q = [i for i in range(len(in_degree)) if in_degree[i] == 0]
        visited = 0
        while q:
            top = q.pop()
            visited += 1
            
            for nei in adj[top]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        return visited == numCourses
