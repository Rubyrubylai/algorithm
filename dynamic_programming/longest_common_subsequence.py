def longest_common_subsequence(s1: str, s2: str) -> int:
  m, n = len(s1), len(s2)
  dp = [[0] * (n + 1) for _ in range(m + 1)]

  for i in range(m):
    for j in range(n):
      if s1[i] == s2[j]:
        # 如果當前字元相等，LCS 增加 1
        dp[i + 1][j + 1] = dp[i][j] + 1
      else:
        # 否則取上方或左方的最大值
        dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

  return dp[m][n]
