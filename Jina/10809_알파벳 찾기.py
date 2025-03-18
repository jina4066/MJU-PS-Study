import sys

input = sys.stdin.readline

s = input().strip()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
lst = [-1] * 26 # 알파벳 위치 저장

for i in range(len(s)):
    index = ord(s[i]) - ord('a') # 알파벳의 인덱스 계산
    # 처음 등장하는 알파벳일 때만 위치 저장
    if lst[index] == -1:
        lst[index] = i

print(' '.join(map(str, lst)))