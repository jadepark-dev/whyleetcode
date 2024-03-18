#
# @lc app=leetcode id=846 lang=python
#
# [846] Hand of Straights
#
# https://leetcode.com/problems/hand-of-straights/description/
#
# algorithms
# Medium (55.87%)
# Likes:    2476
# Dislikes: 171
# Total Accepted:    156.9K
# Total Submissions: 281.1K
# Testcase Example:  '[1,2,3,6,2,3,4,7,8]\n3'
#
# Alice has some number of cards and she wants to rearrange the cards into
# groups so that each group is of size groupSize, and consists of groupSize
# consecutive cards.
#
# Given an integer array hand where hand[i] is the value written on the i^th
# card and an integer groupSize, return true if she can rearrange the cards, or
# false otherwise.
#
#
# Example 1:
#
#
# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
#
#
# Example 2:
#
#
# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.
#
#
#
#
# Constraints:
#
#
# 1 <= hand.length <= 10^4
# 0 <= hand[i] <= 10^9
# 1 <= groupSize <= hand.length
#
#
#
# Note: This question is the same as 1296:
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
#
#

import heapq


# @lc code=start
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """

        # first check if the hand can be divdied by groupSize
        if len(hand) % groupSize:
            return False

        # count the cards
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        # heapify the count to get the card with minimum number
        minH = list(count.keys())  # only keys(card numbers)
        heapq.heapify(minH)

        # iterate while there is heap to organise the deck
        while minH:
            # get the current first card(the smallet card)
            first = minH[0]  # O(1)

            # expect the series of card in current group
            # organise the care series card by card
            for i in range(first, first + groupSize):

                if i not in count:
                    # expected number is not in count, there is hole
                    return False

                # we spent this card
                count[i] -= 1

                if count[i] == 0:
                    # there is hole(next minimum value is not in the deck)
                    if i != minH[0]:
                        return False
                    # there is no card with this number anymore
                    # adjust the heap to get the smallest card
                    # in the next iteration
                    heapq.heappop(minH)

        return True


# @lc code=end
