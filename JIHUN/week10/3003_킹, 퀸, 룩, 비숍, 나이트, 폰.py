correct_pieces = [1, 1, 2, 2, 2, 8]
a = input()
b = list(map(int, a.split()))
c = []
for i in range(6):
    c.append(correct_pieces[i]-b[i])

print(" ".join(map(str, c)))

### B5, 25m ###
# split(), map(), list() 함수에 대해 알지 못했음.
# 위 함수에 대해 공부하며 map이 반환하는 값이 list 형식이 아니기 때문에 list()함수를
# 쓴다는 것도 배울 수 있었음. 또한 join() 함수가 쓰이는 방식을 배우고, 파이썬에서는
# join 함수 대신 print(*c) 로 표현할 수 있다는 것도 알게 되었음.