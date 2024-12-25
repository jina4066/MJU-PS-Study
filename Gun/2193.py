
2193. 이친수

# n = 1일 때 조건을 만족하는 이친수는 1밖에 없으므로 1개
# n = 2, 10 이므로 1개
# n = 3, 100, 101 이므로 2개
# n = 4, 1000, 1001, 1010 이므로 3개
# 피보나치 수열이 보이므로 그대로 구현

n = int(input()) 

# Solution 1

# n = 1일 때 a[2] = 1을 할 수 없으므로 조건문 사용
if n == 1:
    print(1)

else:
    a = [0] * (n + 1)
    a[1] = 1
    a[2] = 1

    for i in range(3, n + 1):
        a[i] = a[i - 2] + a[i - 1]

    print(a[n])


# Solution 2

# a[n] = a[n - 1] + a[n - 2]를 이용한 또 다른 풀이
a, b = 0, 1

for i in range(2, n):
    a, b = b, a + b

print(a + b)
