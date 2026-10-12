class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: 
        prereq = {}
        for p in prerequisites:
            if p[0] not in prereq:
                prereq[p[0]] = []

            prereq[p[0]].append(p[1])

        visited = set()
        def containsCycle(course):
            if course not in prereq or course in visited:
                return False
            if course in visiting:
                return True
            
            visiting.add(course)
            for r in prereq[course]:
                if containsCycle(r):
                    return True
                if r in visiting:
                    visiting.remove(r)
                visited.add(r)



        for course in range(numCourses):
            if course in visited:
                continue
            visiting = set()
            if containsCycle(course):
                return False
            visited.add(course)
        
        return True
