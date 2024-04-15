#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (41.28%)
# Likes:    15623
# Dislikes: 652
# Total Accepted:    1.6M
# Total Submissions: 3.9M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
#
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
#
#
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
#
#
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
#
#
#
# Constraints:
#
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
#
#
#
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
#
#
from collections import List


# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # recursively check if we can complete the given word
        # try all the cells

        ROWS, COLS = len(board), len(board[0])

        visited = set()

        def dfs(i, r, c):
            # reached to the end
            if i == len(word):
                return True

            if (
                # out of bound
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                # been here
                or (r, c) in visited
                # it's not the character we're looking for
                or word[i] != board[r][c]
            ):
                return False

            # add to visited path
            visited.add((r, c))

            # if one of direction has the word we're looking for, return true
            res = (
                dfs(i + 1, r + 1, c)
                or dfs(i + 1, r - 1, c)
                or dfs(i + 1, r, c + 1)
                or dfs(i + 1, r, c - 1)
            )

            # clear the visited path
            visited.remove((r, c))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c):
                    return True

        return False


# @lc code=end
