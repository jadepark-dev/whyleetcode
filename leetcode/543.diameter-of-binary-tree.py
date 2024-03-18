#
# @lc app=leetcode id=543 lang=python
#
# [543] Diameter of Binary Tree
#
# https://leetcode.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (58.79%)
# Likes:    13085
# Dislikes: 879
# Total Accepted:    1.3M
# Total Submissions: 2.2M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the root of a binary tree, return the length of the diameter of the
# tree.
#
# The diameter of a binary tree is the length of the longest path between any
# two nodes in a tree. This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges
# between them.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
#
#
# Example 2:
#
#
# Input: root = [1,2]
# Output: 1
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# -100 <= Node.val <= 100
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
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]

        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            # I need to understand this math part
            res[0] = max(res[0], 2 + left + right)
            return 1 + max(left, right)

        dfs(root)
        return res[0]


# @lc code=end
