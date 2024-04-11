#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (39.25%)
# Likes:    27694
# Dislikes: 3077
# Total Accepted:    2.5M
# Total Submissions: 6.3M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
#
# Example 1:
#
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
#
# Example 2:
#
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
#
# Constraints:
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#

from typing import List


# @lc code=start
class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # run binary search to find the partition pivot point in shorter array

        A, B = nums1, nums2

        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        # binary search on the shorter array to find middle point
        l, r = 0, len(A) - 1

        while True:

            # middle point for A
            midA = l + (r - l) // 2

            # middle point for B(longer array)
            midB = half - midA - 2  #####

            leftAmax = A[midA] if midA >= 0 else float("-infinity")
            rightAmin = A[midA + 1] if (midA + 1) < len(A) else float("infinity")

            leftBmax = (
                B[midB] if midB >= 0 else float("-infinity")
            )  ### out of index, why?
            rightBmin = B[midB + 1] if (midB + 1) < len(B) else float("infinity")

            if leftAmax <= rightBmin and leftBmax <= rightAmin:
                # merged array length is even
                if total % 2 == 0:
                    return (max(leftAmax, leftBmax) + min(rightAmin, rightBmin)) / 2.0
                else:
                    return min(rightAmin, rightBmin)  #####

            elif leftAmax > rightBmin:
                r = midA - 1  #####
            else:
                l = midA + 1

        # it's not log n.. isn't it?
        """
        # merge arrays
        nums = nums1 + nums2

        # sort them(optimal case O(n log n))
        nums.sort()

        length = len(nums)

        # calc mid val
        if length % 2 == 0:
            m1 = nums[length // 2 - 1]
            m2 = nums[length // 2]
            return (float(m1) + float(m2)) / 2.0
        # odd nums, get the middle one
        else:
            return float(nums[length // 2])

        """


# @lc code=end
