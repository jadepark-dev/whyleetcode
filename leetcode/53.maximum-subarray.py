#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Medium (50.58%)
# Likes:    33202
# Dislikes: 1393
# Total Accepted:    3.7M
# Total Submissions: 7.3M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the subarray with the largest sum, and
# return its sum.
#
#
# Example 1:
#
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
#
#
# Example 2:
#
#
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
#
#
# Example 3:
#
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
#
#

# @lc code=start
class Solution:

    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = nums[
            0
        ]  # we don't initialise it with 0 because there are negative nums
        curSum = 0  # for calculation

        for n in nums:  # O(n)
            if curSum < 0:  # if we find an element that makes our sum negative,
                curSum = 0  # reset it.
            curSum += n
            maxSum = max(maxSum, curSum)

        return maxSum


# @lc code=end
