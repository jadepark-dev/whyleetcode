#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (34.11%)
# Likes:    29900
# Dislikes: 2736
# Total Accepted:    3.3M
# Total Submissions: 9.7M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
# Example 1:
#
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
#
#
# Example 2:
#
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#
#
# Example 3:
#
#
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#

from typing import List


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # iterate, i is index, a is value
        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            # same value then before
            if i > 0 and a == nums[i - 1]:
                continue

            left, r = i + 1, len(nums) - 1
            while left < r:
                threeSum = a + nums[left] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[r]])
                    left += 1
                    r -= 1
                    while left < r and nums[left] == nums[left - 1]:
                        left += 1

        return res


# @lc code=end
