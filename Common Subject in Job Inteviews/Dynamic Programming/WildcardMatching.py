class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(s) + 1):
            dp[i][0] = False
        for j in range(1, len(p) + 1):
            dp[0][j] = dp[0][j - 1] and p[j - 1] == "*"
        # print("after init: " , dp)

        for i in range(0, len(s)):
            for j in range(0, len(p)):
                # print(f"(i={i+1},j={j+1})", dp)
                if p[j] == "?" or s[i] == p[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == "*":
                    dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1]
                elif p[j] != s[i]:
                    dp[i + 1][j + 1] = False
                else:
                    raise Exception
        # print("after solve: ", dp)
        return dp[len(s)][len(p)]