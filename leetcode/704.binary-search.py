#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
# https://leetcode.com/problems/binary-search/description/
#
# algorithms
# Easy (57.13%)
# Likes:    11437
# Dislikes: 234
# Total Accepted:    2.2M
# Total Submissions: 3.9M
# Testcase Example:  '[-1,0,3,5,9,12]\n9'
#
# Given an array of integers nums which is sorted in ascending order, and an
# integer target, write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
# Example 1:
#
#
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#
#
# Example 2:
#
#
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^4 < nums[i], target < 10^4
# All the integers in nums are unique.
# nums is sorted in ascending order.
#
#
#


# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # get the mid point, preventing overflow(well python integers are unbounded, but just for best practice)
            m = l + (r - l) // 2
            # just for clarity
            num = nums[m]
            if num == target:
                # we found the target number
                return m
            elif num < target:
                # move the left pointer to the right next to the mid point
                l = m + 1
            elif num > target:
                # move the right pointer to the left next to the mid point
                r = m - 1

        return -1


# @lc code=end
