#
# @lc app=leetcode id=2530 lang=python3
#
# [2530] Maximal Score After Applying K Operations
#
# https://leetcode.com/problems/maximal-score-after-applying-k-operations/description/
#
# algorithms
# Medium (44.98%)
# Likes:    382
# Dislikes: 9
# Total Accepted:    27K
# Total Submissions: 59.6K
# Testcase Example:  '[10,10,10,10,10]\n5'
#
# You are given a 0-indexed integer array nums and an integer k. You have a
# starting score of 0.
#
# In one operation:
#
#
# choose an index i such that 0 <= i < nums.length,
# increase your score by nums[i], and
# replace nums[i] with ceil(nums[i] / 3).
#
#
# Return the maximum possible score you can attain after applying exactly k
# operations.
#
# The ceiling function ceil(val) is the least integer greater than or equal to
# val.
#
#
# Example 1:
#
#
# Input: nums = [10,10,10,10,10], k = 5
# Output: 50
# Explanation: Apply the operation to each array element exactly once. The
# final score is 10 + 10 + 10 + 10 + 10 = 50.
#
#
# Example 2:
#
#
# Input: nums = [1,10,3,3,3], k = 3
# Output: 17
# Explanation: You can do the following operations:
# Operation 1: Select i = 1, so nums becomes [1,4,3,3,3]. Your score increases
# by 10.
# Operation 2: Select i = 1, so nums becomes [1,2,3,3,3]. Your score increases
# by 4.
# Operation 3: Select i = 2, so nums becomes [1,1,1,3,3]. Your score increases
# by 3.
# The final score is 10 + 4 + 3 = 17.
#
#
#
# Constraints:
#
#
# 1 <= nums.length, k <= 10^5
# 1 <= nums[i] <= 10^9
#
#
#
from collections import heapq, List, math


# @lc code=start
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heap.append(-n)

        heapq.heapify(heap)
        # min heap -> heap[0] will be the biggest number in nums

        score = 0
        # randomly pick index but we will pick only index that makes the max
        for i in range(k):
            biggest = -heapq.heappop(heap)

            score += biggest

            ceiled = math.ceil(biggest / 3)
            heapq.heappush(heap, -ceiled)
        return score


# @lc code=end
