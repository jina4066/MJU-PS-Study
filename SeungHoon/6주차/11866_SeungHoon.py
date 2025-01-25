# 요세푸스 문제 0 / Silver 4 / 1h
N, K = map(int,input().split())

arr = []

for i in range(N):
  arr.append(i + 1)

ans = []
index = 0

while len(arr) > 1:
  index += K - 1
  index = index % len(arr)
  ans.append(arr.pop(index))

print("<", end="")
for i in range(len(ans)):
  print(ans[i], end=", ")
print(arr[0], end="")
print(">",end="")

# 1234567
# 124567 3
# 12457 36
# 1457 362
# 145 3627
# 14 36275
# 4 362751
# 위와 같은 형식으로 진행된다
# 인덱스를 계산하는 방법을 계속 고민하다가
# 현재 배열의 길이 % (K - 1)가 인덱스가 된다는 사실을 알아냈다.