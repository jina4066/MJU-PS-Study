# [BOJ] 셀프 넘버 / Silver 5 / 45m
nums = set(range(1,10001))
arr = set()

for i in range(1,10001):
  for j in str(i):
    i += int(j)
  arr.add(i)
  
ans = sorted(nums - arr)
for i in ans:
  print(i)