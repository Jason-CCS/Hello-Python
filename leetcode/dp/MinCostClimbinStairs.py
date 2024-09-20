from typing import List


class Solution:
    # example: cost = [10,15,20]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p1, p2 = 0, 0
        for i in range(len(cost) - 1, -1, -1):
            c = min(p1, p2) + cost[i]
            p2 = p1
            p1 = c

        return min(p1, p2)
