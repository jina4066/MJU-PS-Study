def solution(sticker):
    dp = [0] * len(sticker)
    answer = 0
    if len(sticker) == 1:
        return sticker[0]
    # case 1: the first one is attached
    dp[0] = sticker[0]
    dp[1] = max(sticker[0], sticker[1])
    for i in range(2, len(sticker) - 1):
        dp[i] = max(dp[i - 2] + sticker[i], dp[i - 1])

    answer = dp[-2]

    # case 2: the first one is not attached
    dp[0] = 0
    dp[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp[i] = max(dp[i - 2] + sticker[i], dp[i - 1])

    answer = max(answer, dp[-1])
    return answer