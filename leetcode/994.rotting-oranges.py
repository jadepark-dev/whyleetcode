#
# @lc app=leetcode id=994 lang=python
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Medium (53.82%)
# Likes:    12378
# Dislikes: 388
# Total Accepted:    796.9K
# Total Submissions: 1.5M
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# You are given an m x n grid where each cell can have one of three
# values:
#
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
#
#
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten
# orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange. If this is impossible, return -1.
#
#
# Example 1:
#
#
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#
#
# Example 2:
#
#
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
#
#
# Example 3:
#
#
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer
# is just 0.
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
#
#
#

from collections import deque


# @lc code=start
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # rotten orange position tracker
        q = deque()

        fresh, time = 0, 0

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                orange = grid[r][c]
                # if orange is rotten, put it in the queue
                if orange == 2:
                    q.append([r, c])
                elif orange == 1:
                    fresh += 1
                else:
                    continue

        # for every rotten orange, make orange rotten
        # and put them in the queue again
        # from rotten orange, simultaneously make rotten oranges in 4 dirs
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q and fresh > 0:
            # iterate for every rotten orange
            for _ in range(len(q)):
                curR, curC = q.popleft()

                for dir in dirs:
                    r, c = curR + dir[0], curC + dir[1]
                    if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] != 1:
                        continue

                    grid[r][c] = 2
                    fresh -= 1
                    q.append([r, c])

            time += 1

        return time if fresh == 0 else -1


# @lc code=end
