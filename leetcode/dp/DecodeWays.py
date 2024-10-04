class DecodeWays:
    def solution(self, s: str) -> int:
        return self.memorized_recursion(s)

    def memorized_recursion(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0

            res = dfs(i + 1)  # take [i], i+1 sub-problem
            if (i + 1 < len(s)) and (s[i] == '1' or s[i] == '2' and s[i + 1] in '0123456'):
                res += dfs(i + 2)  # take[i, i+1], i+2 sub-problem

            dp[i] = res
            return res

        return dfs(0)


if __name__ == '__main__':
    print(DecodeWays().solution("10"))
    print(DecodeWays().solution("12"))
    print(DecodeWays().solution("226"))
    print(DecodeWays().solution("06"))
    print(DecodeWays().solution("11106"))
    print(DecodeWays().solution("2611055971756562"))
