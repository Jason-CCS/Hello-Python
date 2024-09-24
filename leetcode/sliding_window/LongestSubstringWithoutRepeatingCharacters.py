class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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
