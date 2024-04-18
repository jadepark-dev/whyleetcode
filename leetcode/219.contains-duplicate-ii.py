#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (44.51%)
# Likes:    6005
# Dislikes: 3052
# Total Accepted:    912.6K
# Total Submissions: 2M
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an integer array nums and an integer k, return true if there are two
# distinct indices i and j in the array such that nums[i] == nums[j] and abs(i
# - j) <= k.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1], k = 3
# Output: true
#
#
# Example 2:
#
#
# Input: nums = [1,0,1,1], k = 1
# Output: true
#
#
# Example 3:
#
#
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5
#
#
#
from collections import List


# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window = set()

        l = 0
        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1

            if nums[r] in window:
                return True

            window.add(nums[r])

        return False


# @lc code=end
