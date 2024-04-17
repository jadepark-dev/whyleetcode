#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (76.97%)
# Likes:    16648
# Dislikes: 266
# Total Accepted:    1.8M
# Total Submissions: 2.3M
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# Example 2:
#
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
#
#
#
from collections import List


# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        dfs, include number or not
        """
        res = []
        subSet = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subSet.copy())
                return

            # include current number
            subSet.append(nums[i])
            backtrack(i + 1)
            subSet.pop()
            # don't include current number
            backtrack(i + 1)

        backtrack(0)

        return res


# @lc code=end
