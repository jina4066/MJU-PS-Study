# 반지 / Silver 5 / 15m
string = input()
N = int(input())

arr = []

for i in range(N):
  line = input()
  ring_line = line
  for j in range(len(string)):
    ring_line += line[j]
  arr.append(ring_line)

count = 0

for i in range(N):
  target =  arr[i]
  if(string in arr[i]):
    count += 1
    
print(count)

# 문자열과 브루트포스로 분류된 문제
# 반지는 원형이므로 실제로 입력받은 문자열에 찾을 문자열이 없더라도, 끝과 시작을 연결해 보면 나올 수 있다.
# 입력받는 문자열 길이가 10으로 한정되어있고
# 실제로 문자열을 두 세번씩 탐색하기 보단
# 찾아야 하는 문자열의 길이만큼만 입력받은 문자열을 확장시켜서 비교하면 된다.