class Node:
    def __init__(self, val):
        self.val = val
        self.nei = set()

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}
        
        for prerequisite in prerequisites:
            courseA, courseB = prerequisite
            if courseA not in courses:
                courses[courseA] = Node(courseA)
            if courseB not in courses:
                courses[courseB] = Node(courseB)
            courses[courseA].nei.add(courseB)

        finished = set()

        def dfs(courseId, visited):
            nonlocal finished
            course = courses[courseId]
            visited.add(courseId)

            for next_course in course.nei:
                if next_course in visited:
                    return False
                dfs(next_course, visited)

            visited.remove(courseId)

            course.nei = set(filter(lambda x: x not in finished, course.nei))
            if len(course.nei) == 0:
                finished.add(courseId)
                return True
            return False

        for courseId in courses.keys():
            if courseId not in finished:
                dfs(courseId, set())
        return len(finished) == len(courses)
