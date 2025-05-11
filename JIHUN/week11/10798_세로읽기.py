grid = []
for _ in range(5):
    row = list(input())  # ✅ split() 제거, 한 줄을 그대로 리스트로 변환
    grid.append(row)

word = []
for i in range(15):
    for j in range(5):
        if i < len(grid[j]):  # ✅ 현재 행에서 i번째 글자가 존재하는지 확인
            word.append(grid[j][i])

result = "".join(word)
print(result)

# 공백을 기준으로 나누는 split을 써서 오류가 났다. 이중반복문의 if 절에서 if grid[j][i]!=""
# 를 썼는데, 오류가 날 것 같아 더 나은 방법인 i 번째 글자 존재 여부를 따지는 방법으로 바꿨다.