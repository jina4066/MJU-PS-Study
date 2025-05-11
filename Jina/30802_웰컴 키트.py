import sys

input = sys.stdin.readline

n = int(input().strip())
s, m, l, xl, xxl, xxxl = map(int, input().split())
# t: 티셔츠 묶음 수, p: 펜 묶음 수
t, p = map(int, input().split()) 

shirtList = [s, m, l, xl, xxl, xxxl]
shirtCount = sum((i + t - 1) // t for i in shirtList)

print(shirtCount)
print(n // p, n % p)