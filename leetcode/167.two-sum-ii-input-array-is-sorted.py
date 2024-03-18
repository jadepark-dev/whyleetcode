#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Medium (60.87%)
# Likes:    11352
# Dislikes: 1374
# Total Accepted:    1.9M
# Total Submissions: 3.1M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given a 1-indexed array of integers numbers that is already sorted in
# non-decreasing order, find two numbers such that they add up to a specific
# target number. Let these two numbers be numbers[index1] and numbers[index2]
# where 1 <= index1 < index2 <= numbers.length.
#
# Return the indices of the two numbers, index1 and index2, added by one as an
# integer array [index1, index2] of length 2.
#
# The tests are generated such that there is exactly one solution. You may not
# use the same element twice.
#
# Your solution must use only constant extra space.
#
#
# Example 1:
#
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We
# return [1, 2].
#
#
# Example 2:
#
#
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We
# return [1, 3].
#
#
# Example 3:
#
#
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We
# return [1, 2].
#
#
#
# Constraints:
#
#
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.
#
#
#

from typing import List


# @lc code=start
class Solution:
    def twoSum(self, numbers, target: int) -> List[int]:
        # Initialize two pointers, 'l' and 'r', pointing to the start and end of the array, respectively.
        # l is shortened form of left
        # r is shortened for of right
        l, r = 0, len(numbers) - 1

        # Use a while loop to iterate until 'l' is less than 'r'.
        while l < r:
            # Calculate the sum of the numbers at positions 'l' and 'r'.
            sum_val = numbers[l] + numbers[r]

            # If the sum is greater than the target, decrement 'r'.
            # Because the input array is sorted in non-decreasing order
            # right value is bigger than left value
            if sum_val > target:
                r -= 1
            # If the sum is less than the target, increment 'l'.
            elif sum_val < target:
                l += 1
            # If the sum is equal to the target, return the indices [l+1, r+1].
            # todo: why do we add 1 to each of them?
            # oh it is instuctued
            # Return the indices of the two numbers, index1 and index2,
            # !added by one as an integer array [index1, index2] of length 2.
            else:
                return [l + 1, r + 1]


# @lc code=end
