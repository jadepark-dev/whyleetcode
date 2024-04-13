#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (34.47%)
# Likes:    38671
# Dislikes: 1796
# Total Accepted:    5.4M
# Total Submissions: 15.7M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Example 2:
#
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
# Example 3:
#
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
#
#
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()  # initialise Set for checking duplicate with Time O(1)

        l = 0
        res = 0

        for r in range(len(s)):  # move right pointer along with the string

            while s[r] in charSet:  # found duplicates

                charSet.remove(s[l])

                l += 1  # move left pointer to the right

            charSet.add(s[r])  # take consider the c in r position

            res = max(
                res, r - l + 1
            )  # compare longest string length with current substring length

        return res

        # identical but with different form for the right pointer

        """
        charSet = set()

        l, r = 0, 0
        res = 0

        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])

            res = max(res, r - l + 1)

            r += 1

        return res

        """


# @lc code=end
