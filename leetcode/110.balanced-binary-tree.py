#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (51.43%)
# Likes:    10379
# Dislikes: 633
# Total Accepted:    1.4M
# Total Submissions: 2.7M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#
#
# Example 3:
#
#
# Input: root = []
# Output: true
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 5000].
# -10^4 <= Node.val <= 10^4
#
#
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # [balanced, height] from the bottom
        def dfs(root):
            if not root:
                return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)

            # height difference
            diff = abs(right[1] - left[1])
            # both children have to be balanced
            balanced = left[0] and right[0] and diff <= 1

            # balanced, and current height
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]


# @lc code=end
