#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (53.37%)
# Likes:    10114
# Dislikes: 466
# Total Accepted:    657.9K
# Total Submissions: 1.2M
# Testcase Example:  '"ABAB"\n2'
#
# You are given a string s and an integer k. You can choose any character of
# the string and change it to any other uppercase English character. You can
# perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter you can
# get after performing the above operations.
#
#
# Example 1:
#
#
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
#
#
# Example 2:
#
#
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length
#
#
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # find longest -> replace fewer characters
        # brute force try -> O(n^2)

        # return the length of the longest substring after mutation
        # create a window, window size - frequent characters <= k
        # count characters, keep the max frequency

        charCount = {}

        l, r = 0, 0
        maxF = 0  # most frequest character count

        for r in range(len(s)):

            charCount[s[r]] = 1 + charCount.get(s[r], 0)
            maxF = max(maxF, charCount[s[r]])

            if (r - l + 1) - maxF > k:  # k is not enough to replace fewer chars
                charCount[s[l]] -= 1
                l += 1  # shift the left pointer

        return r - l + 1


# @lc code=end
