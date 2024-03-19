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
        # dfs
        # a total of numCourses courses you have to take, labeled from 0 to numCourses - 1
        # {0: [], 1: [] ...}
        preMap = {i: [] for i in range(numCourses)}

        # preprocessing:
        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # {0: [], 1: [0]} ...

        visiting = set()

        def dfs(crs):
            # already processing
            if crs in visiting:
                return False
            # we already visited all prerequisites
            # OR no required prerequities
            if preMap[crs] == []:
                return True

            # flag up
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            # flag down
            visiting.remove(crs)
            # empty the preMap
            preMap[crs] = []
            return True

        # in case there are separated courses.
        # duplicated visiting will be prevented by the set "visiting"
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


# @lc code=end
