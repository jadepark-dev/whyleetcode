#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#
# https://leetcode.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (40.31%)
# Likes:    8105
# Dislikes: 5090
# Total Accepted:    1.4M
# Total Submissions: 3.4M
# Testcase Example:  '"the sky is blue"'
#
# Given an input string s, reverse the order of the words.
#
# A word is defined as a sequence of non-space characters. The words in s will
# be separated by at least one space.
#
# Return a string of the words in reverse order concatenated by a single
# space.
#
# Note that s may contain leading or trailing spaces or multiple spaces between
# two words. The returned string should only have a single space separating the
# words. Do not include any extra spaces.
#
#
# Example 1:
#
#
# Input: s = "the sky is blue"
# Output: "blue is sky the"
#
#
# Example 2:
#
#
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing
# spaces.
#
#
# Example 3:
#
#
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single
# space in the reversed string.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s contains English letters (upper-case and lower-case), digits, and spaces '
# '.
# There is at least one word in s.
#
#
#
# Follow-up: If the string data type is mutable in your language, can you solve
# it in-place with O(1) extra space?
#
#


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:

        return " ".join(reversed(s.split()))

        # initial approach
        """
        words = []
        temp = ""

        for i in range(len(s)):
            if s[i].isalnum():
                temp += s[i]
            else:
                if temp != "":
                    words.append(temp)
                    temp = ""

            if i == len(s) - 1:
                if temp != "":
                    words.append(temp)
                    temp = ""

        res = []

        for i in range(len(words) - 1, -1, -1):
            res.append(words[i])
            if i != 0:
                res.append(" ")

        return "".join(res)
        
        """


# @lc code=end
