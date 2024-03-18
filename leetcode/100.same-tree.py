#
# @lc app=leetcode id=100 lang=python
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (60.68%)
# Likes:    10973
# Dislikes: 225
# Total Accepted:    1.9M
# Total Submissions: 3.2M
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given the roots of two binary trees p and q, write a function to check if
# they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.
#
#
# Example 1:
#
#
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
#
#
# Example 2:
#
#
# Input: p = [1,2], q = [1,null,2]
# Output: false
#
#
# Example 3:
#
#
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in both trees is in the range [0, 100].
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
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# @lc code=end
