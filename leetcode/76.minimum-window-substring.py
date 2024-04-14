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

        # create a hashmap to count characters in string t
        # create a hashmap to count characters in current window
        # sliding window
        # extend the window until we find the valid window
        # in the valid window, compare the window size and store the string indices.
        # shrink the left side of the window while we have valid window
        # if we lose our validity, again, extend the right side of the window

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        res, minLength = [-1, -1], float("infinity")

        have, need = 0, len(countT)

        # seize the left pointer on the left edge
        l = 0

        for r in range(len(s)):
            c = s[r]

            # add current character to consideration
            window[c] = 1 + window.get(c, 0)

            # this is the character we're looking for
            # and the count of this character is exactly same
            if c in countT and countT[c] == window[c]:
                have += 1

            # whilst the window is valid, do the thing you need to do

            while have == need:
                # this is possible solution, compare.
                if (r - l + 1) < minLength:
                    res = [l, r]
                    minLength = r - l + 1  # store to compare in the future
                # we're losing the character!
                lc = s[l]
                window[lc] -= 1
                if lc in countT and window[lc] < countT[lc]:
                    have -= 1
                # move the left pointer
                l += 1

        l, r = res
        return s[l : r + 1] if minLength != float("infinity") else ""


# @lc code=end
