#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (46.79%)
# Likes:    8886
# Dislikes: 8243
# Total Accepted:    2.7M
# Total Submissions: 5.8M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. Alphanumeric characters include letters and
# numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
#
# Example 1:
#
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
#
# Example 2:
#
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
# Example 3:
#
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters.
# Since an empty string reads the same forward and backward, it is a
# palindrome.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
#
#
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer approach
        p1 = 0  # p1 starts from the beginning of the string
        p2 = len(s) - 1  # p2 starts from the end of the string

        # let's meet at the middle
        while p1 < p2:

            # convert into lowercase for efficiency
            c1 = s[p1].lower()
            c2 = s[p2].lower()

            # if c1 is not alphanumeric character, move on(increasing p1)
            if not c1.isalnum():
                p1 += 1
            # if c2 is not alphanumeric character, move on(decreasing p2)
            elif not c2.isalnum():
                p2 -= 1
            # check if they're same
            # if they're same, continue to the middle.
            elif c1 == c2:
                p1 += 1
                p2 -= 1
            else:
                # if they're not the same, it's not a palindrom.
                return False
        # after traversing all the characters, return true
        return True

    # @lc code=end

# reverse and compare
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for a in s:
            if a.isalpha() or a.isdigit():
                new += a.lower()
        return new == new[::-1]
"""
