#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (62.73%)
# Likes:    16950
# Dislikes: 633
# Total Accepted:    2M
# Total Submissions: 3.2M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
# p
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
#
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
#
#
from collections import List


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count numbers
        count = {}
        # list with frequency as index
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []
        """
        [1,1,1,2,2,3]
        {
            "1": 3,
            "2": 2,
            "3": 1,
        }
         0   1   2   3   4  5 <-- idx
        [[],[3],[2],[1],[],[]]
        """

        # iterate backwards to find most frequent k elements
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res


# @lc code=end
