#
# @lc app=leetcode id=45 lang=python
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Medium (40.33%)
# Likes:    14118
# Dislikes: 533
# Total Accepted:    1.2M
# Total Submissions: 2.9M
# Testcase Example:  '[2,3,1,1,4]'
#
# You are given a 0-indexed array of integers nums of length n. You are
# initially positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from
# index i. In other words, if you are at nums[i], you can jump to any nums[i +
# j] where:
#
#
# 0 <= j <= nums[i] and
# i + j < n
#
#
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are
# generated such that you can reach nums[n - 1].
#
#
# Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
# step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: nums = [2,3,0,1,4]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].
#
#
#


# @lc code=start
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            _max = 0
            for i in range(l, r + 1):
                _max = max(_max, i + nums[i])
            l = r + 1
            r = _max
            res += 1

        return res


# @lc code=end
