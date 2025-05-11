import sys
input = sys.stdin.readline

n = int(input().strip())
card = (list(map(int,input().strip().split())))

m = int(input())
test = (list(map(int,input().strip().split())))

card_dict = {}

for i in card:
    if i in card_dict:
        card_dict[i] += 1
    else:
        card_dict[i] = 1

for i in test:
    if i in card_dict:
        print(card_dict[i], end=' ')
    else:
        print(0, end=' ')


# 첫 번째 방법 - 시간초과

# import sys
# input = sys.stdin.readline

# n = int(input())
# card = (list(map(int,input().split())))

# m = int(input())
# test = (list(map(int,input().split())))

# result = []

# for i in test:
#     result.append(card.count(i))

# print(*result)
        