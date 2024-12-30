T = int(input())
ans = []
for i in range(T):
  test = list(map(int,input().split()))
  test.sort(reverse = True)
  a = 1 
  b = 1
  for i in range(test[0], test[0] - test[1], -1):
    a = a * i
  for i in range(1, test[1] + 1):
    b = b * i
  ans.append(a // b)
    
for i in range(len(ans)):
  print(ans[i])