#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (54.79%)
# Likes:    28117
# Dislikes: 1637
# Total Accepted:    2.7M
# Total Submissions: 5M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the i^th line are (i, 0) and (i,
# height[i]).
#
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
#
#
# Example 1:
#
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
#
#
# Example 2:
#
#
# Input: height = [1,1]
# Output: 1
#
#
#
# Constraints:
#
#
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
#
#
#


# @lc code=start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxArea = 0

        l, r = 0, len(height) - 1
        while l < r:
            # calculate area
            currArea = min(height[l], height[r]) * (r - l)
            # get the max area
            maxArea = max(maxArea, currArea)
            """ 
                because we already have the max area with that height
                - since it is the lower pointer that means that 
                every other distance that is closer will always be 
                a smaller distance with the same or less height 
                which means smaller area. 
                
                Therefore we do not need to look at every other combination with that pointer.
            """
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxArea


# @lc code=end
