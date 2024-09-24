from typing import List


class Solution:
    """
    Problem: 746
    Difficulty: Easy
    The problem is intended to find the minimum cost to climb a set of stairs where each step has a cost, and next step
    you can choose one step or two step jump.
    """
    # example: cost = [10,15,20]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        This approach is from Leetcode Solutions.
        Complexity: time is O(n), space is O(1).
        """
        p1, p2 = 0, 0
        for i in range(len(cost) - 1, -1, -1):
            c = min(p1, p2) + cost[i]
            p2 = p1
            p1 = c

        return min(p1, p2)
