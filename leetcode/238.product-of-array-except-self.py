#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (65.25%)
# Likes:    21305
# Dislikes: 1285
# Total Accepted:    2.2M
# Total Submissions: 3.4M
# Testcase Example:  '[1,2,3,4]'
#
# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
# You must write an algorithm that runs in O(n) time and without using the
# division operation.
#
#
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
#
#
# Follow up: Can you solve the problem in O(1) extra space complexity? (The
# output array does not count as extra space for space complexity analysis.)
#
#
from collections import List


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        leftToRight = [1] * len(nums)
        rightToLeft = [1] * len(nums)

        l = len(nums)

        for i in range(1, l):
            # fill up leftToRight and rightToLeft
            leftToRight[i] = leftToRight[i - 1] * nums[i - 1]
            rightToLeft[l - i - 1] = rightToLeft[l - i] * nums[l - i]

        for i in range(l):
            res[i] = leftToRight[i] * rightToLeft[i]

        return res


# @lc code=end
