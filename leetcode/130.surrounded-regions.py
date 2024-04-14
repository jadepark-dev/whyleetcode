#
# @lc app=leetcode id=130 lang=python
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (38.85%)
# Likes:    8368
# Dislikes: 1756
# Total Accepted:    672K
# Total Submissions: 1.7M
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given an m x n matrix board containing 'X' and 'O', capture all regions that
# are 4-directionally surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
#
#
# Example 1:
#
#
# Input: board =
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output:
# [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.
#
#
# Example 2:
#
#
# Input: board = [["X"]]
# Output: [["X"]]
#
#
#
# Constraints:
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.
#
#
#


# @lc code=start
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        reverse thinking: remove all the "o"s that cannot be wrapped with "x"s first.
        """
        ROWS, COLS = len(board), len(board[0])

        # directional adjacents
        dirs = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
        ]

        def dfs(r, c):
            # when to stop
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != "O":
                return

            board[r][c] = "T"

            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        for i in range(ROWS):
            for j in range(COLS):
                # run dfs to find edge-started cells
                # find all edge-started "O" and convert them to temp value "T"
                if (i == 0 or i == ROWS - 1 or j == 0 or j == COLS - 1) and board[i][
                    j
                ] == "O":
                    dfs(i, j)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "T":
                    board[i][j] = "O"


# @lc code=end
