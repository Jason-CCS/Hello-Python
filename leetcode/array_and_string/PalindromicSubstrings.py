class Solution:
    """
    Problem: 647
    Difficulty: Medium
    The goal is to calculate and return the number of palindromic substrings in the given text string.
    """
    def countSubstrings(self, s: str) -> int:
        """
        This approach is from AI.
        To be honest, I don't really understand why the AI wrote like this.
        """
        count, length = 0, len(s)

        # 2*n-1 centers. For example, the string "a b c", the centers are "a", "b", "c", "ab", "bc"
        for center in range(2 * length - 1):
            left = center // 2
            right = left + center % 2

            while left >= 0 and right < length and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        return count

    def countSubstrings2(self, s: str) -> int:
        """
        This is my personal approach.
        Example: abcbb
        Approach: use very basic index iterate.
        Complexity: Time is O(n^2), Space is O(1).
        """
        count, length = 0, len(s)

        for center in range(0, length):
            left = right = center
            while left >= 0 and right < length and s[left] == s[right]:  # handle odd number palindrome
                count += 1
                left -= 1
                right += 1
            if center + 1 < length and s[center] == s[center + 1]:  # handle even number string palindrome
                left = center
                right = center + 1
                while left >= 0 and right < length and s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
        return count
