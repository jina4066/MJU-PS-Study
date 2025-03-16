total = int(input())
num = int(input())
price = 0
for i in range(num):
    a, b = map(int, input().split())
    price = price + a*b

if total == price:
    print("Yes")
else:
    print("No")