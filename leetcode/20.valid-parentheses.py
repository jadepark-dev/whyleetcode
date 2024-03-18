#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.41%)
# Likes:    23312
# Dislikes: 1645
# Total Accepted:    4.3M
# Total Submissions: 10.6M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
#
# Example 1:
#
#
# Input: s = "()"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: s = "(]"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
#
#
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # create a pair map to get opener easily from the closer
        pairs = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in pairs:  # check if it is closing
                if stack and stack[-1] == pairs[c]:
                    stack.pop()  # remove the last element
                else:
                    return False  # we always expect the corresponding opener

            else:  # it is opener
                stack.append(c)

        # assume all the matches are popped
        return True if not stack else False


# @lc code=end
