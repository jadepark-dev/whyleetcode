#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (49.72%)
# Likes:    15248
# Dislikes: 402
# Total Accepted:    1.7M
# Total Submissions: 3.3M
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# You are given an m x n integer matrix matrix with the following two
# properties:
#
#
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the
# previous row.
#
#
# Given an integer target, return true if target is in matrix or false
# otherwise.
#
# You must write a solution in O(log(m * n)) time complexity.
#
#
# Example 1:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#
#
# Example 2:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
#
#
#


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # get the row and column count
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            # get the mid row
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                # should I break the loop?
                break

        if not top <= bot:
            return False

        # two pointers in the row
        l, r = 0, COLS - 1

        # re-grap the row we found in the previous loop
        row = (top + bot) // 2

        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True

        return False


# @lc code=end
