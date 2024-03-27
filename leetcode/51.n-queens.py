#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (67.46%)
# Likes:    12037
# Dislikes: 271
# Total Accepted:    694.3K
# Total Submissions: 1M
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle. You
# may return the answer in any order.
#
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space,
# respectively.
#
#
# Example 1:
#
#
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [["Q"]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 9
#
#
#

from typing import List


# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # queen can move vertically, horizontally, and diagonally.
        # meaning; only one queen can be placed in a row, or column, or pos/neg diagonals
        # brute-force queen's position based on rows
        # manage sets for cols, pos/neg diagonals
        # backtrack for each row(recursively try and clean up the flags)
        # return all possible solutions

        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            # base case: reached to the end
            if r == n:
                cp = ["".join(row) for row in board]
                res.append(cp)
                return

            for c in range(n):
                # iterate each column

                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    # found impossible combination, skip the column
                    continue

                # record where we are
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                # put the queen
                board[r][c] = "Q"

                # try next row
                backtrack(r + 1)

                # clean up
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

                # didn't succeed
                board[r][c] = "."

        backtrack(0)
        return res


# @lc code=end
