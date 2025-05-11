# [BOJ] 단어 공부 / Bronze 1 / 20m
string = input()
string = string.lower()

dict = {}
for i in string:
  if(i in dict):
    dict[i] += 1
  else:
    dict[i] = 1

target = max(dict, key = dict.get)
target_count = dict[target]
count = 0
for i in dict:
  if(dict[i] == target_count):
    count += 1

if(count == 1):
  print(target.upper())
else:
  print('?')
  
# Dictionary를 활용해서 푼 문제
# Key, Value쌍으로 각 알파벳이 몇번 나왔는지 저장
# max(dict, key = dict.get)를 이용해 value가 가장 큰 알파벳을 찾고
# target_count = dict[target] 그 알파벳의 value를 찾는다
# dictionary를 돌면서 같은 값을 가지는 알파벳이 있으면 +1
# 최종적으로 카운트가 1이면 출력
# 1 이상이면 ? 출력