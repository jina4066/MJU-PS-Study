# [BOJ] Z / Gold 5 / 3h
N, r, c = map(int,input().split())

def Z(n,r,c, count):
  length = 2 ** n
  half = length // 2
  if(n == 1):
    print(2 * r + c + count)
    return
  
  if(r >= half and c >= half):
    Z(n - 1, r - half, c - half, count + 3 * half * half)
  elif(r >= half > c):
    Z(n - 1, r - half, c, count + 2 * half * half)
  elif(r < half <= c):
    Z(n - 1, r, c - half, count + half * half)
  else:
    Z(n-1, r, c, count)
    
Z(N, r, c, 0)

# 힘들게 풀었다.
# Top-Down 방식으로 풀었음
# 좌표와, 주어진 길이 (2^N)을 기준으로 1,2,3,4 사분면중 어디에 위치한지 파악
# 올바른 사분면으로 재귀를 구현하고, 각 사분면에 맞는 초기값 제공을 위해 count + (N-1)사분면 * 길이 절반 ^ 2 을 파라미터로 넘겨서 결과값에 합산하게 만듬
# 길이가 최소(2)가 되었을 때 좌표는 (2 * r + c) + count로 출력