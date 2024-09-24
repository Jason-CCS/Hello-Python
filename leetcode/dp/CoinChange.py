import collections
from typing import List
from itertools import combinations_with_replacement


class Solution:
    """
    Problem: 322
    Difficulty: Medium
    It's aimed at finding the fewest number of coins that can make up a given amount.
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        This solution is very wrong 'cause you should not expect
        using the largest coin as first one can find the correct coin combination.

        First, sort the coins list, from bigger to smaller.
        sorted_coins = sorted(coins, reverse=True)
        r = amount
        counter = 0
        for d in sorted_coins:
            if ( r >= d)
                quotient = r//d
                counter += quotient
                r = r%d
            if r==0:
                return counter;
        return -1
        :param coins:
        :param amount:
        :return:
        """

        # This solution is very wrong 'cause you should not expect
        # using the largest coin as first one can find the correct coin combination.
        sorted_coins = sorted(coins, reverse=True)
        r = amount
        counter = 0
        for d in sorted_coins:
            if r >= d:
                counter += r // d
                r = r % d
            if r == 0:
                return counter

        return -1

    def coinChange2(self, coins: List[int], amount: int) -> int:
        """
        This approach is from Neetcode tutorial.
        This solution is from https://www.youtube.com/watch?v=H9bfqozjoqs&t=185s.
        This is dp approach.
        Time Complexity: O(amount*len(coin))
        Space Complexity: O(amount)
        :param coins:
        :param amount:
        :return:
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1

    def coinChange3(self, coins: List[int], amount: int) -> int:
        """
        BFS approach
        This approach is TLE.
        :param coins:
        :param amount:
        :return:
        """
        length = len(coins)
        min_num = amount + 1
        coin = 0
        counter = 0
        start_idx = 0
        q = collections.deque([(coin, counter, start_idx, amount)])
        while len(q) > 0:
            coin, counter, start_idx, r = q.popleft()
            r = r - coin
            if r < 0:
                continue
            if r == 0:
                min_num = min(min_num, counter)
            for j in range(start_idx, length):
                q.append((coins[j], counter + 1, j, r))

        return min_num if min_num != amount + 1 else -1


def main():
    coins = [186, 419, 83, 408]
    amount = 6249
    solution = Solution()
    result = solution.coinChange2(coins, amount)
    print(result)


if __name__ == "__main__":
    main()
