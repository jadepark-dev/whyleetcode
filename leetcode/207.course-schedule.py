#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (46.51%)
# Likes:    15832
# Dislikes: 670
# Total Accepted:    1.5M
# Total Submissions: 3.2M
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
#
#
# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
#
#
# Return true if you can finish all courses. Otherwise, return false.
#
#
# Example 1:
#
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
#
#
# Example 2:
#
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you
# should also have finished course 1. So it is impossible.
#
#
#
# Constraints:
#
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
#
#
#


# @lc code=start
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # find cycle in graph
        # topological sort is only possible with DAG(Directed Acyclic Graph)
        # create an adjacency list of prerequisites map

        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # we have premap
        # we need visited set to find cycle condition
        visited = set()

        # run dfs to determine if we can finish all courses without cycle
        def dfs(crs):
            # been here, cycle detected
            if crs in visited:
                return False
            # no prerequisites, we can finish this course
            if preMap[crs] == []:
                return True

            visited.add(crs)
            # new course but there are prerequisites
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        # we passed all courses
        return True


# @lc code=end
