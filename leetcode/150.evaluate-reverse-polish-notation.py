#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (50.77%)
# Likes:    7402
# Dislikes: 1051
# Total Accepted:    971.2K
# Total Submissions: 1.9M
# Testcase Example:  '["2","1","+","3","*"]'
#
# You are given an array of strings tokens that represents an arithmetic
# expression in a Reverse Polish Notation.
#
# Evaluate the expression. Return an integer that represents the value of the
# expression.
#
# Note that:
#
#
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish
# notation.
# The answer and all the intermediate calculations can be represented in a
# 32-bit integer.
#
#
#
# Example 1:
#
#
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#
#
# Example 2:
#
#
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
#
#
# Example 3:
#
#
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
#
#
#
# Constraints:
#
#
# 1 <= tokens.length <= 10^4
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the
# range [-200, 200].
#
#
#


# @lc code=start
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                v1 = stack.pop()
                v2 = stack.pop()
                sum = v1 + v2
                stack.append(sum)
            elif c == "-":
                v1, v2 = stack.pop(), stack.pop()
                stack.append(v2 - v1)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                v1, v2 = stack.pop(), stack.pop()
                stack.append(int(v2 / v1))
            else:
                # only operands
                stack.append(int(c))
        return stack[0]


# @lc code=end
