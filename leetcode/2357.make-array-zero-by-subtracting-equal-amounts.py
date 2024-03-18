#
# @lc app=leetcode id=2357 lang=python
#
# [2357] Make Array Zero by Subtracting Equal Amounts
#
# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/
#
# algorithms
# Easy (72.08%)
# Likes:    1120
# Dislikes: 51
# Total Accepted:    97.6K
# Total Submissions: 135.2K
# Testcase Example:  '[1,5,0,3,5]'
#
# You are given a non-negative integer array nums. In one operation, you
# must:
#
#
# Choose a positive integer x such that x is less than or equal to the smallest
# non-zero element in nums.
# Subtract x from every positive element in nums.
#
#
# Return the minimum number of operations to make every element in nums equal
# to 0.
#
#
# Example 1:
#
#
# Input: nums = [1,5,0,3,5]
# Output: 3
# Explanation:
# In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
# In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
# In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
#
#
# Example 2:
#
#
# Input: nums = [0]
# Output: 0
# Explanation: Each element in nums is already 0 so no operations are
# needed.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
#
#
#
import heapq


# @lc code=start
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ops = 0
        heapq.heapify(nums)
        while any(val > 0 for val in nums):  # list traversal, O(n)
            x = nums[0]
            while x == 0:  # inner loop.
                x = heapq.heappop(nums)
            nums = [n - x if n > 0 else n for n in nums]  # creating a new list, O(n)
            ops += 1

        return ops

    """
    hw's answer - much clear!
    """
    # def minimumOperations(self, nums):
    #     cnt = 0
    #     heapq.heapify(nums)
    #     while nums:
    #         if nums[0] == 0:
    #             heapq.heappop(nums)
    #         else:
    #             cnt += 1
    #             small = heapq.heappop(nums)
    #             nums = [num - small for num in nums]
    #             heapq.heapify(nums)
    #     return cnt


# @lc code=end
