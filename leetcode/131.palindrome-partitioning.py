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

        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                # copy and submit the result
                res.append(part[:])
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s[i : j + 1]):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


# @lc code=end
