# [BOJ] 균형잡힌 세상 / Silver 4 / 20m
while True:
  str = input()
  
  if(str == '.'):
    break
  
  arr = []
  check = True
  
  for i in str:
    if(i in "(["):
      arr.append(i)
    elif(i == ")"):
      if(arr and arr[-1] == "("):
        arr.pop()
      else:
        check = False
        break
    elif(i == "]"):
      if(arr and arr[-1] == "["):
        arr.pop()
      else:
        check = False
        break
  
  if(check and len(arr) == 0):
    print("yes")
  else:
    print("no")
    
# 간단한 스택 문제
# 배열에 왼쪽 괄호를 전부 입력 받은 후
# 오른쪽 괄호가 입력 되었을 때는 배열의 마지막 값을 체크해 매칭이 되면 pop 아니면 no를 출력한다.
# arr[-1]로 배열 마지막 값을 체크한다.
# 최종적으로 배열의 길이가 0이면 yes를 출력한다.