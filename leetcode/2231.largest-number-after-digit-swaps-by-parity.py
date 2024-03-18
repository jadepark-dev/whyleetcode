#
# @lc app=leetcode id=2231 lang=python
#
# [2231] Largest Number After Digit Swaps by Parity
#
# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/description/
#
# algorithms
# Easy (61.22%)
# Likes:    596
# Dislikes: 295
# Total Accepted:    40.4K
# Total Submissions: 66K
# Testcase Example:  '1234'
#
# You are given a positive integer num. You may swap any two digits of num that
# have the same parity (i.e. both odd digits or both even digits).
#
# Return the largest possible value of num after any number of swaps.
#
#
# Example 1:
#
#
# Input: num = 1234
# Output: 3412
# Explanation: Swap the digit 3 with the digit 1, this results in the number
# 3214.
# Swap the digit 2 with the digit 4, this results in the number 3412.
# Note that there may be other sequences of swaps but it can be shown that 3412
# is the largest possible number.
# Also note that we may not swap the digit 4 with the digit 1 since they are of
# different parities.
#
#
# Example 2:
#
#
# Input: num = 65875
# Output: 87655
# Explanation: Swap the digit 8 with the digit 6, this results in the number
# 85675.
# Swap the first digit 5 with the digit 7, this results in the number 87655.
# Note that there may be other sequences of swaps but it can be shown that
# 87655 is the largest possible number.
#
#
#
# Constraints:
#
#
# 1 <= num <= 10^9
#
#
#
import heapq


# @lc code=start
class Solution(object):
    def largestInteger(self, num):
        oddNumberHeap = []
        evenNumberHeap = []

        for digit in str(num):  # Push onto heaps
            digit = int(digit)
            if digit % 2 == 0:
                heapq.heappush(evenNumberHeap, -digit)
            else:
                heapq.heappush(oddNumberHeap, -digit)

        maxNum = ""  # max number will be a string, we will later convert to int
        for digit in str(num):
            digit = int(digit)

            # If digit is even, we will put the max even number here
            if digit % 2 == 0 and evenNumberHeap:
                maxEvenNum = -heapq.heappop(evenNumberHeap)
                maxNum += str(maxEvenNum)

            # If digit is odd, we will put the max odd number here.
            elif digit % 2 == 1 and oddNumberHeap:
                maxEvenNum = -heapq.heappop(oddNumberHeap)
                maxNum += str(maxEvenNum)

            # If parity not found, we keep the same number
            else:
                maxNum += str(digit)

        return int(maxNum)


# @lc code=end
