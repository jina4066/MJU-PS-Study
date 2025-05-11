# 수 찾기 / Silver 4 / 40m
N = int(input())

arr1 = list(map(int,input().split()))

M = int(input())

arr2 = list(map(int,input().split()))

arr1.sort()

for i in arr2:
  lt, rt = 0, N-1
  isExist = False
  
  while lt <= rt:
    mid = (lt + rt) // 2
    if(i == arr1[mid]):
      isExist = True
      print(1)
      break
    elif (i > arr1[mid]):
      lt = mid + 1
    else:
      rt = mid -1
      
  if not isExist:
    print(0)
    
# 그냥 이중 반복문 쓰니 시간 초과가 뜸
# 이진 탐색을 이용하는 문제
# 1. 비교할 배열을 정렬
# 2. 인덱스 시작과 끝 값 설정
# 3. 중간 값부터 탐색 시작
# 4. 크기의 대소에 따라 배열의 시작, 끝 값을 중간값에서 조절
# 5. 값을 찾으면 1을 출력
# 6. 값을 못찾으면 0을 출력