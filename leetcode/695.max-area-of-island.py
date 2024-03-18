#
# @lc app=leetcode id=695 lang=python
#
# [695] Max Area of Island
#
# https://leetcode.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (71.85%)
# Likes:    9790
# Dislikes: 198
# Total Accepted:    832.8K
# Total Submissions: 1.2M
# Testcase Example:  '[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]'
#
# You are given an m x n binary matrix grid. An island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You
# may assume all four edges of the grid are surrounded by water.
#
# The area of an island is the number of cells with a value 1 in the island.
#
# Return the maximum area of an island in grid. If there is no island, return
# 0.
#
#
# Example 1:
#
#
# Input: grid =
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected
# 4-directionally.
#
#
# Example 2:
#
#
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.
#
#
#


# @lc code=start
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # get the rows and cols
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()

        def dfs(r, c):
            if (
                # check the index bound first
                r < 0  # out of bound
                or r == ROWS  # out of bound
                or c < 0  # out of bound
                or c == COLS  # out of bound
                # and you can do other things
                or grid[r][c] == 0  # it's not land
                or (r, c) in visited  # been here -> optimised T.C
            ):
                return 0

            # calculate the area
            return (
                1
                + dfs(r + 1, c)  # top cell
                + dfs(r - 1, c)  # bottom cell
                + dfs(r, c + 1)  # right cell
                + dfs(r, c - 1)  # left cell
            )

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))

        return area


# @lc code=end
