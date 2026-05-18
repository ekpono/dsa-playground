# https://leetcode.com/problems/course-schedule/

"""
How it works
You have a list of prerequisites for each course
and each prerequisite tells you which course it depends on
[0,         1]
course      prerequisite course
Before a course is taken, the prerequisite needs to be taken first
if you can take all the courses then return true
but if course prerequite takes back to a course that is already being taken, then you have a loop and you can't take all the courses, return false


"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Take:
        # [[1,0],[2,1],[0,2]]

        # Write it as:
        # course 0, 1, 2
        # 1 needs 0
        # 2 needs 1
        # 0 needs 2

        # Now literally follow it with your finger:

        # 0 → 2 → 1 → 0

        # Boom.
        # Loop.

        #  check all the courses it depends on
        # then check what those depend on
        # and so on

        # [[1,4],[2,4],[3,1],[3,2]]
        # 1 → 4
        # 2 → 4
        # 3 → 1 → 4
        # 3 → 2 → 4
        # 4 → []

        graph = collections.defaultdict(list)
        state = [0] * numCourses

        for a, b in prerequisites:
            graph[a].append(b)


        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True

            state[course] = 1

            for nei in graph[course]:
                if not dfs(nei):
                    return False

            state[course] = 2
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True