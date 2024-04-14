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
        # minimum number of minutes, or -1

        # why bfs => adjacent oranges first(simultaneously)
        time = 0

        # manage rotten oranges
        rottens = deque()

        # store the count of fresh oranges
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                status = grid[i][j]

                if status == 2:
                    # store rotten orange's coord
                    rottens.append([i, j])
                elif status == 1:
                    # count the fresh oranges
                    fresh += 1

        # 4-directionally adjacent
        dirs = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
        ]

        while rottens and fresh > 0:

            for i in range(len(rottens)):

                # get the current rotten orange and remove it from the queue
                r, c = rottens.popleft()

                for dr, dc in dirs:
                    # next cell
                    row, col = dr + r, dc + c

                    if (
                        row < 0
                        or row == len(grid)
                        or col < 0
                        or col == len(grid[0])
                        or grid[row][col] != 1
                    ):
                        # skip the rotten or empty cell or out of boundary
                        continue

                    # new rotten orange!
                    grid[row][col] = 2
                    rottens.append([row, col])

                    # reduce the count of fresh orange
                    fresh -= 1

            # increase the time
            time += 1

        return time if fresh == 0 else -1


# @lc code=end
