#[BOJ] 좋은 단어 / Silver 4 / 30m
N = int(input())

count = 0

for i in range(N):
  string = input()
  arr = [0]
  for j in range(len(string)):
    length = len(arr)
    if(arr[length - 1] == string[j]):
      arr.pop(length - 1)
    else:
      arr.append(string[j])
  if(len(arr) == 1):
    count += 1

print(count)

# 처음에 리스트 마지막 값을 제거하기 위해 arr.remove(string[j]) 이딴식으로 작성했다가 틀렸다.
# 저건 배열의 특정한 값을 제거하기 때문에 옳지 않다.
# arr.pop(index)를 쓰자
# 나머지는 괄호 문제와 크게 다를게 없었다.