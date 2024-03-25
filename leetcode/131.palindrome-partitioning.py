#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (67.04%)
# Likes:    12259
# Dislikes: 432
# Total Accepted:    777.3K
# Total Submissions: 1.2M
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome. Return all possible palindrome partitioning of s.
#
#
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
# Input: s = "a"
# Output: [["a"]]
#
#
# Constraints:
#
#
# 1 <= s.length <= 16
# s contains only lowercase English letters.
#
#
#

from typing import List


# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # backtracking is a smarter way to do brute-forcing
        res = []
        part = []

        def dfs(i):  # i is the index of current character
            if i >= len(s):  # base case - we've  reached to end of the string.
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrom(s, i, j):
                    part.append(s[i : j + 1])
                    dfs(j + 1)  # recursive
                    part.pop()  # clean-up

        dfs(0)
        return res

    def isPalindrom(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True


# @lc code=end
