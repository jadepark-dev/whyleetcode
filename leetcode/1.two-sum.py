#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (51.81%)
# Likes:    55662
# Dislikes: 1914
# Total Accepted:    12.8M
# Total Submissions: 24.4M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# You can return the answer in any order.
#
#
# Example 1:
#
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#
# Example 2:
#
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
#
# Example 3:
#
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
#
#
#
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time
# complexity?
#
from collections import List


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMaps = {}

        # build hash table with number and its index
        for i in range(len(nums)):
            numMaps[nums[i]] = i

        for i in range(len(nums)):
            # check if sum up to target
            complement = target - nums[i]
            # check if we have candidates
            if complement in numMaps and numMaps[complement] != i:
                return [i, numMaps[complement]]

        return []


# @lc code=end
