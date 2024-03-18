#
# @lc app=leetcode id=572 lang=python
#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (47.53%)
# Likes:    8014
# Dislikes: 481
# Total Accepted:    803.6K
# Total Submissions: 1.7M
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# Given the roots of two binary trees root and subRoot, return true if there is
# a subtree of root with the same structure and node values of subRoot and
# false otherwise.
#
# A subtree of a binary tree tree is a tree that consists of a node in tree and
# all of this node's descendants. The tree tree could also be considered as a
# subtree of itself.
#
#
# Example 1:
#
#
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -10^4 <= root.val <= 10^4
# -10^4 <= subRoot.val <= 10^4
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

    def sameTree(self, p, q):
        if not p and not q:  # both trees are empty
            return True

        # mind the order of conditions
        if not p or not q or p.val != q.val:
            return False

        # mind the usage of recursive function call in Python
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)

    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        # edge cases
        if not subRoot:  # subTree is null
            return True

        if not root:  # subTree is not null, but main Tree is null
            return False

        # same tree?
        if self.sameTree(root, subRoot):
            return True

        # recursion
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# @lc code=end
