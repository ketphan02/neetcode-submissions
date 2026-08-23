class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i: [] for i in range(numCourses)}
        print(courses)
        for prerequisite in prerequisites:
            courseA, courseB = prerequisite
            courses[courseA].append(courseB)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED for _ in range(numCourses)]
        def dfs(node):
            state = states[node]
            if state == VISITED: return True
            if state == VISITING: return False

            states[node] = VISITING

            for nxt in courses[node]:
                if not dfs(nxt):
                    return False
            
            states[node] = VISITED
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return False

        return True


            

