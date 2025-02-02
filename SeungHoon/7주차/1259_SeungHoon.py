# [BOJ] 팰린드롬수 / Bronze 1 / 20m
while True:
  num = input()
  if(int(num) == 0):
    break
  check = 1
  target = len(num) // 2
  end = len(num) - 1
  for i in range(target):
    if(num[i] != num[end]):
      print('no')
      check = -1
      break
    else:
      end -= 1
  if(check == 1):
    print('yes')
    
# 간단한 문제
# 배열의 끝과 시작을 중간값 까지 비교해서
# 하나라도 다르면 no를 출력한다.

# if (num == num[::-1]):
#   print('yes')
# else:
#   print('no')
# 이렇게 슬라이싱을 쓰면 더 간단하다.