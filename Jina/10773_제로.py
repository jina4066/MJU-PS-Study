k = int(input())

number = []
sum = 0

for _ in range(k):
    num = int(input())
    if num != 0:
        number.append(num)
    else:
        number.pop()

for i in range(len(number)):
    sum += number[i]

print(sum)