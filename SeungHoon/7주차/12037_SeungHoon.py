# [BOJ] Polynesiaglot (Small1) / Silver 5 / 2h
T = int(input())

MOD = 1000000007
for t in range(1, T + 1):
  C, V, L = map(int,input().split())
  dp = [[0] * 2 for _ in range(16)]
  dp[1][0] = V
  dp[1][1] = C
  for i in range(2, L + 1):
    dp[i][0] = (dp[i - 1][0] * V + dp[i - 1][1] * V) % MOD
    dp[i][1] = (dp[i - 1][0] * C) % MOD
  print(f"Case #{t}:", dp[L][0] % MOD)
  
# 생각을 좀 한 DP 문제
# 문제 조건은 
# 1. 단어는 모음이나 자음으로 시작할 수 있다.
# 2. 모음 뒤에는 모음이나 자음 둘 다 와도 된다
# 3. 자음 뒤에는 모음만 올 수 있다
# 4. 단어는 모음으로 끝난다.
# 점화식을 세우면
# 모음으로 끝나는 경우 dp[i][0] = 자음으로 끝난 경우의 수 * 모음의 수 + 모음으로 끝난 경우의 수 * 모음의 수
# 자음으로 끝나는 경우 dp[i][1] = 자음으로 끝난 경우의 수 * 모음의 수
# 언제나처럼 출력값 형식 때문에 3~4번 틀렸다