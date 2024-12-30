N, M = map(int, input().split())
array = list(map(int, input().split()))

array.sort()

# 이렇게 풀면 틀린다
# ans_array = []
# for i in range(len(array)):
#  for j in range(i + 1, len(array)):
#    if(total_sum > M):
#      break
#    for k in range(j + 1, len(array)):
#      total_sum = total_sum + array[k]
#      if(total_sum > M):
#        break
#      else:
#        ans_array.append(total_sum)

# 괜히 이전 루프에서 초기화 하는게 아니라 마지막 루프에서 초기화
ans_array = []
for i in range(len(array)):
 for j in range(i + 1, len(array)):
   for k in range(j + 1, len(array)):
     total_sum = array[i] + array[j] + array[k]
     if(total_sum > M):
       break
     else:
       ans_array.append(total_sum)
       
ans_array.sort(reverse = True)

print(ans_array[0])
