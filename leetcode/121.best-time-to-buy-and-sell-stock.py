#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (53.49%)
# Likes:    29957
# Dislikes: 1071
# Total Accepted:    4.3M
# Total Submissions: 8.1M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
#
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you
# cannot achieve any profit, return 0.
#
#
# Example 1:
#
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you
# must buy before you sell.
#
#
# Example 2:
#
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit =
# 0.
#
#
#
# Constraints:
#
#
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4
#
#
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxP = 0
        # declare the lowest
        lowest = prices[0]
        # iterate through prices, find lowest and calculate max profit
        for price in prices:
            if price < lowest:
                lowest = price
            maxP = max(maxP, price - lowest)
        return maxP

        # brute force way... prices * prices -> O(n^2)
        # so two pointer technique
        # always i < j, so initially 0, 1
        # so 0 <= i < len(prices) - 1, 1 <= j < len(prices) if profitable

        """ bare two pointer alike(but same technique)
        res = 0

        i, j = 0, 1

        while j < len(prices):
            profit = prices[j] - prices[i]

            if profit > 0:
                res = max(res, profit)
            else:
                i = j

            j += 1

        return res
        """

        """
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
            
        return max_profit
        """

# @lc code=end
