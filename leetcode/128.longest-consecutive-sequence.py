#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (47.31%)
# Likes:    19272
# Dislikes: 922
# Total Accepted:    1.6M
# Total Submissions: 3.4M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#
# Example 1:
#
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
#
#
# Example 2:
#
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
#
#


# @lc code=start
class Solution:
    def longestConsecutive(self, nums) -> int:
        # initialise value for comparison
        longest = 0
        # it's just set... to remove duplications
        num_set = set(nums)

        for n in num_set:
            # check negative consecutive number is in the set
            if (n - 1) not in num_set:  # identify the start of new consecutive sequence
                # if it's not, let's start with the length = 1
                # !meaning this is the start of new sequence
                length = 1
                # todo: why it's n+length?
                # 4 -> 4 + 1 = 5
                # 4 -> 4 + 2 = 6
                # ah, to check the consecutive following numbers..
                # anyway it is started with 1, it naturally increase the number by one.
                while (n + length) in num_set:
                    length += 1
                longest = max(longest, length)

        return longest


# @lc code=end
