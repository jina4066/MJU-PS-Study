array = list(map(int, input().split()))

for i in range(-999, 1000):
  for j in range(-999, 1000):
    if(array[0] * i + array[1] * j == array[2] and array[3] * i + array[4] * j == array[5]):
      print(i, j)
      exit()
    
# -999 ~ 999 까지 범위이므로 -999, 1000으로 설정해줘야 함
