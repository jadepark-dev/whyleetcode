#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (42.68%)
# Likes:    17582
# Dislikes: 715
# Total Accepted:    1.3M
# Total Submissions: 3.1M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates)
# is included in the window. If there is no such substring, return the empty
# string "".
#
# The testcases will be generated such that the answer is unique.
#
#
# Example 1:
#
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
# from string t.
#
#
# Example 2:
#
#
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
#
#
# Example 3:
#
#
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
#
#
#
# Constraints:
#
#
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
#
#
#
# Follow up: Could you find an algorithm that runs in O(m + n) time?
#
#


# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        chars = {}

        # create a hashmap for t
        for c in t:
            chars[c] = 1 + chars.get(c, 0)

        l = 0  # doesn't have to be 0? where is the start?

        # find the left side
        for i in range(len(s)):
            if s[i] in chars:
                l = i
                break

        print(chars)
        for r in range(l, len(s)):

            # extend the window(r += 1, for loop do the job)
            # check if new char is in character
            # reduce the number of that char
            # if we have char empty, return the miminum string[l:r+1] found
            # right edge of the window

            if s[r] in chars and chars[s[r]] > 0:
                chars[s[r]] -= 1
                if chars[s[r]] == 0:
                    del chars[s[r]]

            if not chars:
                return s[l : r + 1]

        return ""
        # oh minimum...


# @lc code=end
