import sys
input = sys.stdin.readline

sugar = int(input())
bag = 0

while sugar >= 0:
    if sugar % 5 == 0:
        bag += (sugar // 5)
        print(bag)
        break
    sugar -= 3
    bag += 1

else:
    print(-1)

# sugar이 5의 배수라면 몫을 출력하고, 아니라면 3씩 빼며 sugar가 음수가 되기 전까지 반복한다. 