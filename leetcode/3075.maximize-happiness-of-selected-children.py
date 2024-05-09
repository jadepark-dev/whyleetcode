# looks like the api is not working, so I will just copy the code here
from collections import List, heapq


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # sort the happiness to get maximum happiness
        heap = []
        heapq.heapify(heap)

        for h in happiness:
            heapq.heappush(heap, -h)

        turn = 0

        res = 0

        while k > 0 and heap:
            # select one child
            h = -heapq.heappop(heap)
            cur = h - turn if h - turn > 0 else 0

            res += cur

            turn += 1
            k -= 1

        return res
