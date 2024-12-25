# 다섯개의 문자열 저장할 리스트 생성
words = []

# 다섯개의 문자열 입력받아 리스트에 저장
for i in range(5):
    word = input().strip()
    words.append(word)

# 세로로 읽은 문자열 저장할 변수
result = ''

# 가장 긴 문자열 길이 구하기
max_len = max(len(word) for word in words)

for i in range(max_len):  # 가장 긴 문자열 길이만큼 반복
    for j in range(5):    # 다섯개의 문자열을 세로로 읽어서 result에 추가
        if i < len(words[j]):    # 글자가 있는 경우에만 실행
            result += words[j][i]

print(result)