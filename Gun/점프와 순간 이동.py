def solution(n):
    answer = 1
    while n > 2:
        if n % 2 == 0:
            n //= 2
        else:
            answer += 1
            n -= 1
    return answer

# 비트 수를 이용한 풀이 (최적)
def solution(n):
    return bin(n).count('1')

# DP 풀이 (시간 초과)
def solution(n):
    while n % 2 == 0:
        n //= 2
    
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i // 2] if i % 2 == 0 else dp[i - 1] + 1

    return answer