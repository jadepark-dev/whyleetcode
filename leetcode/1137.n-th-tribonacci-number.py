#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#
# https://leetcode.com/problems/n-th-tribonacci-number/description/
#
# algorithms
# Easy (63.44%)
# Likes:    4147
# Dislikes: 181
# Total Accepted:    663.1K
# Total Submissions: 1M
# Testcase Example:  '4'
#
# The Tribonacci sequence Tn is defined as follows:
#
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#
# Given n, return the value of Tn.
#
#
# Example 1:
#
#
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
#
#
# Example 2:
#
#
# Input: n = 25
# Output: 1389537
#
#
#
# Constraints:
#
#
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 -
# 1.
#
#


# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        # recursive with cache
        cache = {}
        cache[0], cache[1], cache[2] = 0, 1, 1

        def rec(n):
            if n in cache:
                return cache[n]
            res = rec(n - 1) + rec(n - 2) + rec(n - 3)

            cache[n] = res

            return res

        return rec(n)


# @lc code=end
