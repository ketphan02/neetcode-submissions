class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for _ in range(numCourses)]
        adj = {i: [] for i in range(numCourses)}

        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        
        stack = [i for i in range(len(indegree)) if indegree[i] == 0]
        while stack:
            top = stack.pop()
            numCourses -= 1

            for nei in adj[top]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    stack.append(nei)

        return numCourses == 0
        