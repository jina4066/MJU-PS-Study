# 속도 위반 / Silver 5 / 1h
N, M = map(int,input().split())

pro = []

for i in range(N):
  L , V = map(int,input().split())
  pro.append((L,V))
  
real = []

for i in range(M):
  L , V = map(int,input().split())
  real.append((L,V))
  
pro_start = 0
pro_end = 0

real_start = 0
real_end = 0

ans = 0

i = 0
j = 0

while i < N and j < M:
  pro_length, pro_speed = pro[i]
  real_length, real_speed = real[j]
  
  pro_end = pro_start + pro_length
  real_end = real_start + real_length
  
  if(real_speed > pro_speed):
    ans = max(ans, real_speed - pro_speed)
  
  if pro_end < real_end:
    pro_start = pro_end
    i += 1
  elif pro_end > real_end:
    real_start = real_end
    j += 1
  else:
    pro_start = pro_end
    real_start = real_end
    i += 1
    j += 1
  
print(ans)

# 시작점과 끝점 위치를 잘 갱신해야함