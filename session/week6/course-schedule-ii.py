# https://leetcode.com/problems/course-schedule-ii/

"""
- Get the prerequisite to be a graph
- Go through number of course start from the first one
- In each dfs check if you are currently checking the current course (cyclic)
- Cheeck if the course has already been checked
- Mark the course that you are currently checking
- Loop through each group and check its neigbours
- After the loop mark course as checked and update response with the course

"""
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        state = [0] * numCourses
        graph = {}
        response = []

        for a, b in prerequisites:
            if a not in graph:
                graph[a] = []

            graph[a].append(b)

        def dfs(course):

            if state[course] == 1:
                return False

            if state[course] == 2:
                return True

            state[course] = 1

            for prereq in graph.get(course, []):
                if not dfs(prereq):
                    return False

            state[course] = 2
            response.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return response

