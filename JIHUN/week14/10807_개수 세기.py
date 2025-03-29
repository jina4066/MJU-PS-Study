a = int(input())
numbers = list(map(int, input().split()))
b = int(input())
count = 0
for i in numbers:
    if i == b:
        count += 1
print(count)
