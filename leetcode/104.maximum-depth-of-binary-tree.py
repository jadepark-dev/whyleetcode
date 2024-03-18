#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (75.02%)
# Likes:    12455
# Dislikes: 212
# Total Accepted:    2.9M
# Total Submissions: 3.9M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#
#
# Example 2:
#
#
# Input: root = [1,null,2]
# Output: 2
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 10^4].
# -100 <= Node.val <= 100
#
#
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        # calculate root(current) node -> 1 + recursively compare lefties and righties
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# @lc code=end
