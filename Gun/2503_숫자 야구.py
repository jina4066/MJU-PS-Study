import sys
from itertools import permutations

def solution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(permutations(list(range(1, 10)), 3))
    
    for _ in range(n):
        num, s, b = map(int, input().split())
        temp = []
        
        for check in nums:
            s_cnt, b_cnt = 0, 0

            for i in range(3):
                if str(check[i]) == str(num)[i]:
                    s_cnt += 1
                if str(check[i]) != str(num)[i] and str(check[i]) in list(str(num)):
                    b_cnt += 1

            if (s, b) == (s_cnt, b_cnt):
                temp.append(check)
                
        nums = temp

    print(len(nums))

if __name__ == '__main__':
    solution()
