a, b = map(int, input().split())
numbers = list(map(int, input().split()))
c = []
for i in numbers:
    if i < b:
        c.append(str(i))
print(" ".join(c))