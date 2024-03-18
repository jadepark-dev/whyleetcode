#
# @lc app=leetcode id=417 lang=python
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (55.05%)
# Likes:    7183
# Dislikes: 1421
# Total Accepted:    447.9K
# Total Submissions: 812.7K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# There is an m x n rectangular island that borders both the Pacific Ocean and
# Atlantic Ocean. The Pacific Ocean touches the island's left and top edges,
# and the Atlantic Ocean touches the island's right and bottom edges.
#
# The island is partitioned into a grid of square cells. You are given an m x n
# integer matrix heights where heights[r][c] represents the height above sea
# level of the cell at coordinate (r, c).
#
# The island receives a lot of rain, and the rain water can flow to neighboring
# cells directly north, south, east, and west if the neighboring cell's height
# is less than or equal to the current cell's height. Water can flow from any
# cell adjacent to an ocean into the ocean.
#
# Return a 2D list of grid coordinates result where result[i] = [ri, ci]
# denotes that rain water can flow from cell (ri, ci) to both the Pacific and
# Atlantic oceans.
#
#
# Example 1:
#
#
# Input: heights =
# [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans,
# as shown below:
# [0,4]: [0,4] -> Pacific Ocean
# [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean
# [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
# [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
# [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean
# [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean
# [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean
# ⁠      [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the
# Pacific and Atlantic oceans.
#
#
# Example 2:
#
#
# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and
# Atlantic oceans.
#
#
#
# Constraints:
#
#
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 10^5
#
#
#


# @lc code=start
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        """
            Reach to the both of ocean
            -> Create two sets of the highest cells that can be reached from cells near ocean
            -> Traverse cells and check if the cell can be found in the both of cells.
        """

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        # take r,c and visited(generalised set), and prevHeight for comparing
        def dfs(r, c, visited, prevHeight):

            # don't go further if the cell is out of boundary,
            # or the height is smaller so we can't move on.
            if (
                (r, c) in visited
                or r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return

            # add to visited to 1. prevent duplicated visit 2. check later for determine if the cell is included in the both sets
            visited.add((r, c))

            # move on! worry about the index boundary at the first stage of dfs function
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(COLS):
            # cells on the top edge
            dfs(0, c, pac, heights[0][c])
            # cells on the bottom edge
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            # cells on the left edge
            dfs(r, 0, pac, heights[r][0])
            # cells on the right edge
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        # traverse all the cells to find the solution
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res


# @lc code=end
