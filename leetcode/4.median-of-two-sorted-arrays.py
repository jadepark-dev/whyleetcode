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

        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # keep the array A smaller
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            # middle pointer for the shorter array(A)
            i = (l + r) // 2
            # middle pointer for the longer array(B)
            # we already know the half
            j = half - i

            Aleft = A[i] if i >= 0 else -float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")

            Bleft = B[j] if j >= 0 else -float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                # right partition is correct
                # odd(홀수)
                if total % 2 == 1:
                    return min(Aright, Bright)
                # even length
                else:
                    return max(Aleft, Bleft) + min(Aright, Bright) / 2

            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

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
