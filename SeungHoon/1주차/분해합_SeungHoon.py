N = int(input())

arr = []
for i in range(1, N):
  sum = 0
  init = i
  while init > 0:
    sum = sum + (init % 10)
    init //= 10
  if(sum + i == N):
    arr.append(i)

if arr:
  print(arr[0])
else:
  print(0)
