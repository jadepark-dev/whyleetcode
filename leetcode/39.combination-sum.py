#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (70.86%)
# Likes:    18454
# Dislikes: 400
# Total Accepted:    1.9M
# Total Submissions: 2.6M
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen
# numbers sum to target. You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen
# numbers is different.
#
# The test cases are generated such that the number of unique combinations that
# sum up to target is less than 150 combinations for the given input.
#
#
# Example 1:
#
#
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple
# times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
#
#
# Example 2:
#
#
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
#
#
# Example 3:
#
#
# Input: candidates = [2], target = 1
# Output: []
#
#
#
# Constraints:
#
#
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40
#
#
#
from collections import List


# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # return all unique combinations
        # candidate can be used multiple times

        res = []

        def bt(i, cur, total):

            # if sum exceeds target, terminate
            if i >= len(candidates) or total > target:
                return

            # if comb adds up to sum, append solution
            if total == target:
                res.append(cur.copy())
                return

            cur.append(candidates[i])
            bt(i, cur, total + candidates[i])
            cur.pop()
            # stay on current index or increase

            bt(i + 1, cur, total)

        bt(0, [], 0)
        return res


# @lc code=end
