#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-sudoku/description/
#
# algorithms
# Medium (59.25%)
# Likes:    10303
# Dislikes: 1080
# Total Accepted:    1.4M
# Total Submissions: 2.4M
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:
#
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
# without repetition.
#
#
# Note:
#
#
# A Sudoku board (partially filled) could be valid but is not necessarily
# solvable.
# Only the filled cells need to be validated according to the mentioned
# rules.
#
#
#
# Example 1:
#
#
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
#
#
# Example 2:
#
#
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner
# being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it
# is invalid.
#
#
#
# Constraints:
#
#
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.
#
#
#


# @lc code=start

""" 
    

    

    
"""


class Solution:
    def isValidSudoku(self, board) -> bool:
        # 1)It initializes an empty list called "res", which will be used to store all the valid elements in the board.
        res = []
        # 2)It loops through each cell in the board using two nested "for" loops.
        for i in range(9):
            for j in range(9):
                # For each cell, it retrieves the value of the element in that cell and stores it in a variable called "element".
                element = board[i][j]
                if element == ".":
                    continue
                # 3)If the element is not a dot ('.'), which means it's a valid number,
                # the method adds three tuples to the "res" list:

                res += [
                    # The first tuple contains the row index (i) and the element itself.
                    (
                        i,
                        element,
                    ),
                    # The second tuple contains the element itself and the column index (j).
                    (element, j),
                    # The third tuple contains the floor division of the row index by 3 (i // 3),
                    # the floor division of the column index by 3 (j // 3), and the element itself.
                    # This tuple represents the 3x3 sub-grid that the current cell belongs to.
                    (i // 3, j // 3, element),
                ]

        # 4)After processing all the cells, the method checks if the length of "res" is equal to the length of the set of "res".
        return len(res) == len(set(res))


# @lc code=end
