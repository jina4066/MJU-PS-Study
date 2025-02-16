import sys
from itertools import product

def solution():
    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(str, input().split()))
    answered = False

    # n의 자릿수만큼 돌기
    for i in sorted(product(a, repeat = len(str(n))), reverse = True):
        num = ""
        for v in list(i):
            num += v
        if n >= int(num):
            print(num)
            answered = True
            break
   
    # 답이 안 나왔으면 n의 자릿수 - 1 중 가장 큰 값으로 정하기
    if not answered:
        print(max(a) * (len(str(n)) - 1))
    
if __name__ == '__main__':
    solution()
