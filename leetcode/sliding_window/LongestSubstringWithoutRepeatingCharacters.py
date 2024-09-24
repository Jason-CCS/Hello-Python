class Solution:
    """
    Problem: 3
    Difficulty: Medium
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Using sliding window approach.
        window:[start, end].
        We iterate through the string by index end, and move the start when we find the same character in map table.
        Sometimes we will find that the index get from map table is smaller than current start index.
        When this happens, we will use line 21, max(start, d[s[end]]+1) to keep the start idx at the original position.
        Time: O(n) as we only iterate the end idx from 0~n-1.
        Space: O(distinct characters) as we use dictionary to store the characters.
        :param s:
        :return:
        """
        max_length, d, start, end = 0, {}, 0, 0

        while end < len(s):
            if s[end] in d:
                start = max(start, d[s[end]] + 1)
            max_length = max(max_length, end - start + 1)
            d[s[end]] = end
            end += 1
        return max_length


def main():
    result = Solution().lengthOfLongestSubstring("abba")
    print(result)


if __name__ == "__main__":
    main()
