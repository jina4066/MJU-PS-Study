import sys

N = int(sys.stdin.readline())
lst = []

for i in range(N):
    lst.append(sys.stdin.readline().strip())

set_list = set(lst)
lst = list(set_list)
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)

#set은 단순히 리스트를 set으로 바꿔줄 뿐 변수에 저장해주지 않기 때문에, set_list라는 변수를 선언하여 따로 저장해주고 그 값을 다시 list로 변환해줬다.

