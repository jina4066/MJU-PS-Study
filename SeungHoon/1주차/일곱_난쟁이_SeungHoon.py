array = []

for i in range(9):
    array.append(int(input()))

array.sort()

total_sum = sum(array)

ans1, ans2 = -1, -1

for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if total_sum - (array[i] + array[j]) == 100:
            ans1, ans2 = array[i], array[j]
            break
    if ans1 != -1 and ans2 != -1:
        break

# 값을 지울 때 array.pop(ans) 식으로 index로 제거하려 하면 오류가 남
array.remove(ans1)
array.remove(ans2)

for num in array:
    print(num)
