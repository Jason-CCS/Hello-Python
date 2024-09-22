from typing import List

"""
Problem: 213
Difficulty: Medium
The code aims to solve the 'House Robber II' problem, which seeks the maximum sum of non-adjacent elements for
 a circular list of values.
"""
class Solution:
    """
    Example: nums = [1, 2, 3, 1, 5, 7]
    Approaches: Greedy
    Looking into the array, we can understand nums[4] can be from nums[2] or nums[1], and even from nums[0].
    But if it is from nums[0], why not come from nums[0]->nums[2]->nums[4]. This maybe will lead greater value.
    Therefore, try to compare from nums[2] or nums[1] is the key to distinguish which stolen path can lead to
    maximum sum of money.
    I will divide them into two part. One is start from index 0. The other is start from index 1.
    If we start from Index 0, then we can iterate the list to index=len(nums)-2 only
    cause 'len(nums)-1' is the adjacent house of index 0.
    And if we start from index 1, then we can iterate the list to the last one.
    Pseudocode:
    if len(nums)==1
      return nums[0]
    if len(nums)==2
     return max(nums[0], nums[1]
    if len(nums)>2

    p3=nums[0], p2=nums[1], p1=nums[0]
    for i=0 ~ len(nums)-2: // handle circular issue
      zero_start_sum = max(nums[i]+p2, nums[i]+p3)
      p3=p2
      p2=p1
      p1=maxSum
      return max(zero_start_sum, p2)  p2 is previous index which might be greater than max_sum.

    p3=nums[0], p2=nums[1], p1=nums[0]
    for i=1 ~ len(nums)-1:
      one_start_sum = max(nums[i]+p2, nums[i]+p3)
      p3=p2
      p2=p1
      p1=maxSum
      return max(one_start_sum, p2)
    """

    def rob(self, nums: List[int]) -> int:

        def max_sum(self, start_idx, end_idx, nums: List[int]) -> int:
            max_sum = 0
            p1, p2, p3 = 0, 0, 0
            for i in range(start_idx, end_idx):
                max_sum = max(p2 + nums[i], p3 + nums[i])
                p3 = p2
                p2 = p1
                p1 = max_sum
            return max(max_sum, p2)

        length = len(nums)
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        start_from_zero_sum = max_sum(self, 0, length - 1, nums)
        start_from_one_sum = max_sum(self, 1, length, nums)

        return max(start_from_zero_sum, start_from_one_sum)


print(Solution().rob([2, 3, 2]))
print(Solution().rob([1, 2, 3, 1]))
print(Solution().rob([1, 2, 3]))
print(Solution().rob([200, 3, 140, 20, 10]))
print(Solution().rob([1, 2, 3, 1, 5, 7]))
